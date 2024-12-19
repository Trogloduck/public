Monitors, controls incoming and outgoing network traffic

![[Pasted image 20241219141151.png]]

- **Stateful Firewall**: can keep track of state of active connections and make decisions based on traffic context
- **Built-in high availability and availability zones**: ensure continuous operation, minimal downtime, higher availability and resilience by distributing resources across separate zones
- **Network and application level filtering**
- **Source and destination network address translation ([[NAT]])**
	- **SNAT** (Source Network Address Translation) translates private IP address of network resource (source) to Azure public IP address, identifies and allows traffic **from virtual network to internet**
	- **DNAT** (Destination Network Address Translation), public IP address used to access specific services inside network is translated and filtered to private IP addresses of the resource on virtual network (destination), allows traffic **from internet to private** resources
- **Threat intelligence**: feed, known malicious IP addresses and domains can be filtered
- **Logging and Monitoring**: keep track of firewall activity and diagnose issues
- **Integration with Azure Services**: Azure Virtual Networks, Azure Policy, Azure Security Center
___

#### Copilot integration

Conditions
- Firewall configured with resource specific structured logs for IDPS (Intrusion Detection and Prevention System), sent to Log Analytics workspace
- User has role permissions
- Firewall plugin in Security Copilot turned on