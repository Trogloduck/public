### Table of contents
- [[#Network Monitoring]]
- [[#Zeek]]
- [[#Architecture]]
- [[#Frameworks]]
- [[#Outputs]]
- [[#Practical Use]]
- [[#Logs]]

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

**Zeek-Snort differences**

| Tool            | Zeek                                                                                                                                          | Snort                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Focus           | Network analysis                                                                                                                              | Signatures                                                              |
| Detection       | Events                                                                                                                                        | Signature patterns and packets                                          |
| Pros            | - In-depth traffic analysis<br>- Threat hunting<br>- Detect complex threats<br>- Scripting language, event correlation<br>- Easy to read logs | - Easy to write rules<br>- Cisco supported rules<br>- Community support |
| Cons            | - Hard to use<br>- Analysis done out of Zeek                                                                                                  | - Hard to detect complex threats                                        |
| Common Use Case | - Network monitoring<br>- In-depth traffic investigation<br>- Intrusion detecting in chained events                                           | - Intrusion detection and prevention<br>- Stop known attacks/threats    |

### Architecture
[[#Table of contents|Back to the top]]

2 main layers: Event Engine & Policy Script Interpreter
- **Event Engine**: where packets are processed (divided into parts: source, destination addresses, protocol identification, session analysis, file extraction), "event core" describing event without details
- **Policy Script Interpreter**: where semantic analysis is conducted, event correlations using scripts

![[Pasted image 20250304104254.png]]

### Frameworks
[[#Table of contents|Back to the top]]

- Extended functionality in scripting layer
- More flexibility and compatibility with other network components
- Each framework $\rightarrow$ specific use case

| Frameworks |                      |            |                 |                |
| ---------- | -------------------- | ---------- | --------------- | -------------- |
| Logging    | Notice               | Input      | Configuration   | Intelligence   |
| Cluster    | Broker Communication | Supervisor | GeoLocation     | File Analysis  |
| Signature  | Summary              | NetControl | Packet Analysis | TLS Decryption |
### Outputs
[[#Table of contents|Back to the top]]

Wide range of logs: **50+ logs in 7 categories**

Running Zeek $\rightarrow$ it automatically investigates the traffic or given [[pcap]] and generates logs
- pcap: logs in working directory
- Zeek as service: logs in default log path, `/opt/zeek/logs/`

### Practical Use
[[#Table of contents|Back to the top]]

Run
- as **service** for **live** network **monitoring**
- against **pcap** file for packet **investigation**

**`zeek -v`**: check Zeek **version**

Running Zeek as service requires **ZeekControl** module which requires superuser permissions (**`sudo su`**)

**`zeekctl`**
- `status`
- `start`
- `stop`

| **Parameter** | **Description**                           |
| ------------- | ----------------------------------------- |
| **-r**        | Reading option, read/process a pcap file. |
| **-C**        | Ignoring checksum errors.                 |
| **-v**        | Version information.                      |
| **zeekctl**   | ZeekControl module.                       |
*Example:* `zeek -C -r sample.pcap` *generates logs based on sample.pcap*

___
### Logs
[[#Table of contents|Back to the top]]

