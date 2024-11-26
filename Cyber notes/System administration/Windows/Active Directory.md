#### Intro
Active Directory Domain Services (AD-DS) is an identity and access management platform

#### Database and Objects
It's basically a **database** of **objects**: users, groups, computers (or other devices), ...

#### Attributes
All objects have **attributes**. For instance, a user has a 1st name, last name, email address, ...

#### Schema
The **schema** defines the types of objects and the attributes they can have within the database.

#### Organizational Units
Users and other objects can be structured into **Organizational Units** (OUs), according to department, location, function, etc. 

#### Domains and Forests
For a large corporation, AD can help organize a main domain into child domains, which together form a **forest**.

#### Global Catalog 
The Global Catalog is a distributed data repository that contains a searchable, partial representation of every object in every domain within a forest.

#### Trust Relationships
Trust relationships between domains allow users in one domain to access resources in another domain.

#### Replication of AD database
In a scenario where a company has several servers across different locations, the AD database will be replicated on each server:
- Intra-site replication: automatic replication within one location
- Inter-site replication: replication across sites
	- IP: fast replication thanks to today's large broadband
	- SMTP: slower but can be scheduled

#### Security and Authentication 
AD-DS also plays a crucial role in security by providing authentication and authorization services.

#### Group Policies
AD-DS allows administrators to define group policies for managing the configuration and security settings of user and computer environments.

___

>*With Azure AD, the database is not on the server, it's in Azure's cloud.* 
>*It is structured in a similar way to the file explorer on Windows.*