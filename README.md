# Insight the NCM  
To be honest, NCM is definitely the dream network software. I always (have to) look forward to some improvements in "security auditing" features.

## Prepare  
Before continuing, please make the following preparations.

1. System  
   Ubuntu 21.04 x64 (2Core; 8GB; Virtual Machine; 4 NIC)

   > Change SSH services port instead of `22/tcp`.

2. Install NCM   
   [Installation and Getting Started](https://www.manageengine.com/network-configuration-manager/help/installation-getting-started.html#Inst_Linux)

3. Deploy `pgAdmin4` web.  
   [Install pgAdmin4 in Virtual Machine](https://www.pgadmin.org/download/pgadmin-4-apt/)

4. Start NCM  
   See [`run.md`](run.md) .

---

## Scenerios
### S1 - About the Vul. database. 

- [x] Models relationship reverse-enginnering.   

  1. [The UML for NCM `OpManagerDB` diagram](firmVuls/OpManager_NCM_DB.uml)  
  2. [Some Intresting Designs](firmVuls/Analysis.md)  


- [x] Migrate the vulnerability `public.ncmfvvulnerabilitydetails.summary` to the language other than English.  
  -  [`translate_summary.py`](firmVuls/translate_summary.py)  


- [x] Take over this the datasets upgrade of the features . (For complianting CAC No. 66 regulations.)
  1. Prepare dataset from CNVD.
  2. Insert into table.
  3. Set a new endpoint for Vulnerability database upgrade.


### S2 - Upgrade networking visualization as daemon.

- [ ] Reference and what I (and others) expected.
- [ ] Link layer information collection.
- [ ] Runtime protocol parse.


### S3 - Some new attempts on security auditing strategies.

- [ ] A Statically Vulnerability Assessment.
- [ ] The principle of redemption priorities caculate.
- [ ] Make extensions, which is not only working with REST API.

### S4 - "Crossing the network" by NCM. 

> (Hope it's possible and can be proved in production env.)


---

As you needed, please buy and support the commerical version Z\*h\* NCM software if you have enough budget. This git repo. only for learning use.

## Attentions
Unless you know the relevant password correctly, it is risky to use a modified version of NCM in a production environment.
