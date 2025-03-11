**SSE**: Security Service Edge
- ***limit lateral movement*** through compromised VPN tunnel
- perimeter for ***internet-based assets***
- ***remote work***, branches

**Global Secure Access**: enables routing through [[#Entra private access]] and [[#Entra Internet Access]]

#### Entra private access

Replace legacy VPN, limit lateral movement, reduce access

Enterprise app serves as **container** for set of private resources
- **Quick Access**: determine which resources to add to "container" ("Quick Access app")
![[Pasted image 20241218100915.png]]

- **Global Secure Access ap**p ("per-app access"): create multiple "containers", assign users, groups, conditional access

#### Entra Internet Access

**SWG** -- Secure Web Gateway: protects users from web-based threats, filtering traffic, enforcing security policies

Entra Internet Access: ***identity-centric SWG for SaaS***

Key features
- Protection against **identity/token theft**
	- Compliant network: authentication through Entra ID, data protected by CAE (Continuous Access Evaluation)
	- **CAE**: ensure user access up-to-date and secure
- Tenant restrictions
- Internet Access traffic forwarding profile policies: control which websites can be accessed
- Web content filtering

#### Global Secure Access Dashboard

- **Global Secure Access snapshot**: *# users, devices, apps secured through service*
- **Alerts and notifications**: *identify suspicious activities/trends*
	- **Unhealthy remote network**: *one or more device links disconnected*
	- **Increased** external tenants **activity**
	- **Token** and **device inconsistency**: *original token used on different device*
	- **Web content blocked**: *access to the website has been blocked*
- **Usage profiling**: pattern (internet access, private access, MS 365)
- **Cross-tenant access** (all in last 24h)
	- Sign-ins: *\# sign-ins through Entra ID to MS services*
	- Total distinct tenants: *\# of distinct tenant IDs*
	- Unseen tenants: *\# distinct tenant IDs that were seen in last 24h, but not in previous 7 days*
	- Users: *\# distinct user sign-ins to other tenants*
	- Devices: *\# distinct devices that signed in to other tenants*
- **Web category filtering**: *top categories blocked/allowed by service*
- **Device status**: *(in)active deployed devices*

