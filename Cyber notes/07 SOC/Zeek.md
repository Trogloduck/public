### Table of contents
- [[#Network Monitoring]]
- [[#Zeek]]
	- [[#Zeek Architecture]]
	- 

___
### Network Monitoring
[[#Table of contents|Back to the top]]

**Monitoring**: watch, overview, save traffic for investigation
- **Uptime**: availability
- Connection **quality**: performance
- Network **traffic balance** and **management**: configuration

**NSM** (Network Security Monitoring): focus on network **anomalies**, intrusion **detection** and **response**

**Network anomalies**:
- Rogue hosts
- Encrypted traffic
- Suspicious service and port usage
- Malicious/suspicious traffic patterns

___
### Zeek
[[#Table of contents|Back to the top]]

*Network monitoring tool -- Traffic analyzer, security, performance, troubleshooting*

Both ***open source*** and ***commercial***: some forks are ***enterprise-ready*** ([***Corelight***](https://corelight.com/products/compare-to-zeek) for instance)

Wide range of logs: **50+ logs in 7 categories**

**Zeek-Snort differences**

| Tool            | Zeek                                                                                                                                          | Snort                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Focus           | Network analysis                                                                                                                              | Signatures                                                              |
| Detection       | Events                                                                                                                                        | Signature patterns and packets                                          |
| Pros            | - In-depth traffic analysis<br>- Threat hunting<br>- Detect complex threats<br>- Scripting language, event correlation<br>- Easy to read logs | - Easy to write rules<br>- Cisco supported rules<br>- Community support |
| Cons            | - Hard to use<br>- Analysis done out of Zeek                                                                                                  | - Hard to detect complex threats                                        |
| Common Use Case | - Network monitoring<br>- In-depth traffic investigation<br>- Intrusion detecting in chained events                                           | - Intrusion detection and prevention<br>- Stop known attacks/threats    |

#### Zeek Architecture
[[#Table of contents|Back to the top]]

2 main layers: Event Engine & Policy Script Interpreter
- **Event Engine**: where packets are processed (divided into parts: source, destination addresses, protocol identification, session analysis, file extraction), "event core" describing event without details
- **Policy Script Interpreter**: where semantic analysis is conducted, event correlations using scripts

![[Pasted image 20250304104254.png]]

