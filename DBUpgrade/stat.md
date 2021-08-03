# Compare NVD data within CNVD dataset
**Data Last Updated: 08/01/2021**

## Summary
- Total NVD Records in NCM: **9159**   
  (Upgrade file: 0d508d703b837effa0ec25b76c6f4a86)  

- Records from CNVD (Only Networking and OT field.): **3978**  
  Containing 47% (1885 rows) data same as NCM dataset. 
  - With 1388 CVE rows in CNVD dataset is NOT included in NCM.

## Difference
NCM contains too **many un-useful records**. Keywords like "`Huawei Smart Phone`".

Now we have **11044** deduplicated rows data:

- Data in NCM: 83%
- Data in CNVD: 17% (Need to be Merged(or Appended) into DB!)

## Data Structure

SOURCE | vulid | cveid | basescore2 | basescore3 | serverityid | summary | published_date | last_updated_date | cvssv2_metrices | cvssv3_metrices |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| in NCM | x | x | x | x |(1-4) | x | x | x | x | x | x | x | 
| CNVD | x | (Number/cveNumber) |  |  | (-/L/M/H) | x | (submitTime) | (openTime) | | | 



---
(I hope some officially sources org. will improve their data values!)


## DDL of `ncmfvvulnerabilitydetails`
```sql
-- auto-generated definition
create table ncmfvvulnerabilitydetails
(
    vulid             bigint not null
        constraint ncmfvvulnerabilitydetails_pk
            primary key,
    cveid             citext not null
        constraint ncmfvvulnerabilitydetails_64506573_c
            check (length((cveid)::text) <= 100),
    basescore2        real   not null,
    basescore3        real   not null,
    severityid        bigint not null,
    summary           citext not null,
    published_date    bigint not null,
    last_updated_date bigint not null,
    cvssv2metrices    citext
        constraint ncmfvvulnerabilitydetails_480082765_c
            check (length((cvssv2metrices)::text) <= 100),
    cvssv3metrices    citext
        constraint ncmfvvulnerabilitydetails_1327371698_c
            check (length((cvssv3metrices)::text) <= 100)
);

```
For complication CNVD dataset:
```sql
-- auto-generated definition
create table ncmfvvulnerabilitydetails
(
    vulid             bigint not null
        constraint ncmfvvulnerabilitydetails_pk
            primary key,
    cveid             citext not null
        constraint ncmfvvulnerabilitydetails_64506573_c
            check (length((cveid)::text) <= 100),
    basescore2        real   , -- Ignore 2 columns.
    basescore3        real   , 
    severityid        bigint not null,
    summary           citext not null,
    published_date    bigint not null,
    last_updated_date bigint not null,
    cvssv2metrices    citext
        constraint ncmfvvulnerabilitydetails_480082765_c
            check (length((cvssv2metrices)::text) <= 100),
    cvssv3metrices    citext
        constraint ncmfvvulnerabilitydetails_1327371698_c
            check (length((cvssv3metrices)::text) <= 100)
);

```