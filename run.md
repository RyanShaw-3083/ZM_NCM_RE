# Steps to start NCM

## Run in normal mode first
Execute `<NCM_Install_Directory>/bin/run.sh` and access NCM with `http://<HOST>:8090/`.

## Change Postgres settings

1. Stop Postgres server.  
   `<NCM_Install_Directory>/bin/stop_PgSQL.sh`

2. Modify `<NCM_Install_Directory>/pgsql/data/global/pg_hba.conf`
    ```
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            trust
    ```
3. Start Postgres server.
   `<NCM_Install_Directory>/bin/start_PgSQL.sh`

As above steps to start NCM. We have bypassed check and won't receive the log as below:
```
Auth Mode cannot be trust. Kindly change and restart.
```

---

## The database settings and password (random and encrypted)

file: `<NCM_Install_Directory>/conf/database_params.conf`
```
# login username for database if any
username=dbuser

# login password for the database if any
password=e54d4e973aa96f8b95aa79493281c0758d7f6b02c5514bbd486d3a844f404c432f662d7d040514694f723f52db626346d004b855ed1cd770f2224c84db21355de2986216

```

Option `password` set with 136 characters (entropy-rich).
```
$x = "e54d4e973aa96f8b95aa79493281c075"
$y = "8d7f6b02c5514bbd486d3a844f404c43"
$z = "2f662d7d040514694f723f52db626346d004b855ed1cd770f2224c84db21355de2986216"
```

In data file:
```
rouser
md57470807e1de5bc6af2a9f48e4ba544284
postgres
md54bfe49880f149201aeb89f3c67e46f51/
dbuser
md5f5b24033f34e6c5cf714cc8bbef276d5
postgres
md5bfc7967f361158ccd13b365548a58b67
```

- [x] Analysis `<NCM_Install_Directory>/lib/AdvPersistence.jar`.

    ```java
    ...

    public class DefaultDBPasswordProvider implements DBPasswordProvider {
    ...
    public String getPassword(Object context) throws PasswordException {
        String password = null;
        ...
            try {
                return cryptTag != null ? CryptoUtil.decrypt(password, algo, cryptTag) : CryptoUtil.decrypt(password, algo);
            } catch (Exception var6) {
                LOGGER.info("Decryption Failed! " + var6.getMessage());
                return password;
            }
        ...
    }

    ```

