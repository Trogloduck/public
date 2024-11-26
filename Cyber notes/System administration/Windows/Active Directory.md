Active Directory Domain Services (AD-DS) is an identity platform

It's basically a **database** of **objects**: users, groups, computers (or other devices), ...

Users can be structured into **Organizational Units**, according to department, location, function, etc. 

All objects have **attributes**. For instance, a user has 1st name, a last name, an e-mail address, ...

The ensemble of users in the database is called the **schema**. 

In a scenario where a company has several servers across different locations, AD can be used to replicate the databases on its servers:
- Intra-site replication: automatic replication in one location
- Inter-site replication: replication across sites

For a large corporation, AD will help divide a main domain into children domains. 

>*With Azure AD, the database is not on the server, it's in Azure's cloud.* 
>*It is structured in a similar way to the file explorer on Windows.*
___

