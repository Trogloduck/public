Microsoft Entra ID (previously Azure Active Directory): SSO service, active directory # I will refer to it as "Entra" for concision

>Identity Secure Score: percentage score indicating how aligned with Microsoft's best practice recommendation you are

- **Tenant**: org's Entra instance containing organizational objects such as users, groups, devices, application registrations, and access and compliance policies; has unique ID and domain name
- **Directory**: inside tenant, logical container holding users, groups, applications, devices; only one directory per tenant
- **Multi-tenant**: org that has >1 tenant
___
#### Types of identities

- **User**: person
- **Device**: mobile phone, computer, ...
- **Workload**: software-based (apps, VMs, containers, ...)

Device and Workload: Machine identities
___
#### User

Authentication
- **Internal**: user's account in host org's Entra
- **External**: user's account in other org's Entra

Typical assignation
- **Internal member**: employee
- **External guest**: consultants, vendors, partners
- **External member**: multi-tenant
- **Internal guest**: distributor, supplier, vendor that needs to collaborate inside the org. Less common, more common to use **B2B** (Business To Business) collaboration

![[Pasted image 20241217103832.png]]

>External members and internal guests: B2B collaborators
___
#### Workload

Software workload authentication and access to other services and resources

- **Service principal**: identity for app
- **Managed identities**: automatically managed service principal
	- **System**-assigned: tied to lifecycle of Azure resource
	- **User**-assigned: tied to use of one user, can be used for several Azure resources
___
#### Devices

- Entra **registered** devices: **BRYOD** (Bring Your Own Device) scenario, register device in Entra without org account to sign in
- Entra **joined** devices: joined through org account used to sign in
- Entra **hybrid joined** devices: joined to on-premised AD and Entra, use org account to sign in
___
#### Groups

Groups identities that have same access needs
- **Security**: permission needs, users, devices, workloads, groups; created by Entra admin
- **Microsoft 365**: collaboration needs, only users; created by anyone

**Dynamic membership**: rules for automatic add/remove of identities in/from groups
___
#### Hybrid ID

- **Inter-directory**: provisioning identity between 2 different directory services systems; typically, from AD to Entra
- **Synchronization**: matching on-premise identity with cloud
___
#### External ID

![[Pasted image 20241217113534.png]]

![[Pasted image 20241217113622.png]]

![[Pasted image 20241217113820.png]]

CIAM: Customer Identity and Access Management
![[Pasted image 20241217113950.png]]
