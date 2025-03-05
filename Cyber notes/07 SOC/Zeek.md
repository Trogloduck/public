### Table of contents
- [[#Network Monitoring]]
- [[#Zeek]]
- [[#Architecture]]
- [[#Frameworks]]
- [[#Outputs]]
- [[#Practical Use]]
- [[#Logs]]
- [[#Signatures]]

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

[Log files](https://docs.zeek.org/en/current/script-reference/log-files.html), [Corelight cheatsheet](https://corelight.com/products/zeek-data/)

Most commonly used logs:

| Update Frequency | Log Name             | Description                                    |
| ---------------- | -------------------- | ---------------------------------------------- |
| Daily            | `known_hosts.log`    | Hosts that completed TCP handshakes            |
| Daily            | `known_services.log` | Services used by hosts                         |
| Daily            | `known_certs.log`    | SSL certificates                               |
| Daily            | `software.log`       | Software used on network                       |
| Per Session      | `notice.log`         | Anomalies detected by Zeek                     |
| Per Session      | `intel.log`          | Traffic contains malicious patterns/indicators |
| Per Session      | `signatures.log`     | Triggered signatures                           |


Example use of logs in 4 steps of investigation:

| **Overall Info**     | **Protocol Based** | **Detection**    | **Observation**      |
| -------------------- | ------------------ | ---------------- | -------------------- |
| _conn.log_           | _http.log_         | _notice.log_     | _known_host.log_     |
| _files.log_          | _dns.log_          | _signatures.log_ | _known_services.log_ |
| _intel.log_          | _ftp.log_          | _pe.log_         | _software.log_       |
| _loaded_scripts.log_ | _ssh.log_          | _traceroute.log_ | _weird.log_          |
1. **Overall info**: connections, shared files, loaded scripts
2. **Protocol Based**: suspicious indicator found $\rightarrow$ focus on specific protocol
3. **Detection**: use prebuild/custom scripts and signature outcomes for further investigation
4. **Observation**: summary of hosts, services, software, unexpected activity stats

For correlation, better to use specialized tool like Splunk

**`zeek-cut`**: select column to display
*Example*: `cat conn.log | zeek-cut uid proto id.orig_h`

___
### Signatures
[[#Table of contents|Back to the top]]

| ID        | Conditions                                                                                                                                                                     | Action                                                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Unique ID | - **Header**: filtering packet headers for specific source/destination addresses, protocol, port numbers<br>- **Content**: filtering packet payload for specific value/pattern | - **Default** action: create **`signature.log`** file in case of signature **match**<br>- **Additional** action: trigger Zeek **script** |


Most common filtering conditions:

| Condition Field               | Available Filters                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Header**                    | - **src-ip**: Source IP.<br>- **dst-ip**: Destination IP.<br>- **src-port**: Source port.<br>- **dst-port**: Destination port.<br>- **ip-proto**: Target protocol. Supported protocols; TCP, UDP, ICMP, ICMP6, IP, IP6                                                                                                                                                         |
| **Content**                   | - **payload:** Packet payload.  <br>- **http-request:** Decoded HTTP requests.  <br>- **http-request-header:** Client-side HTTP headers.  <br>- **http-request-body:** Client-side HTTP request bodys.  <br>- **http-reply-header:** Server-side HTTP headers.  <br>- **http-reply-body:** Server-side HTTP request bodys.  <br>- **ftp:** Command line input of FTP sessions. |
| **Context**                   | **same-ip:** Filtering the source and destination addresses for duplication.                                                                                                                                                                                                                                                                                                   |
| Action                        | **event:** Signature match message.                                                                                                                                                                                                                                                                                                                                            |
| **Comparison  <br>Operators** | **==, !=, <, <=, >, >=**                                                                                                                                                                                                                                                                                                                                                       |
| **NOTE**                      | Filters accept string, numeric and **regex** values.                                                                                                                                                                                                                                                                                                                           |

Run Zeek with signature: **`zeek -C -r sample.pcap -s sample.sig`**

***Example signatures***:
```Zeek
signature http-password {
	ip-proto == tcp
	dst-port == 80
	payload /.*password.*/
	event "Cleartext Password Found!"
}
# signature: Signature name.
# ip-proto: Filtering TCP connection.
# dst-port: Filtering destination port 80.
# payload: Filtering the "password" phrase.
# event: Signature match message.
```
*looks for the keyword "password" in communications transmitted with HTTP (clear text)*

```Zeek
signature ftp-username {
	ip-proto == tcp
	ftp /.*USER.*/
	event "FTP Username Input Found!"
}

signature ftp-brute {
	ip-proto == tcp
	payload /.*530.*Login.*incorrect.*/
	event "FTP Brute-force Attempt!"
}
```
*looks for failed attempt at FTP logging in as user*

