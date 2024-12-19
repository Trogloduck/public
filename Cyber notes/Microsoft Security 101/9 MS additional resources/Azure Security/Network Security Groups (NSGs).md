Filter network traffic to/from Azure resources in VNet

Security rules components
- **Name**: describe purpose
- **Priority**: lower number before higher
- **Source/destination**: IP address (or range), service tag, application security group
- **Protocol**: TCP, UDP, ICMP, ...
- **Direction**: Inbound vs Outbound
- **Port range**
- **Action**: Allow vs Deny

Firewall complements NSG
- **NSG**: network-level protection within VNet in each subscription
- **Firewall**: network and application-level protection across subscriptions and VNets