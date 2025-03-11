### Table of contents
- [[#Network Monitoring]]
- [[#Zeek]]
- [[#Architecture]]
- [[#Intro to Frameworks]]
- [[#Outputs]]
- [[#Practical Use]]
- [[#Logs]]
- [[#Signatures]]
- [[#Scripts]]
	- [[#Selecting info]]
	- [[#Scripts and Signatures]]
	- [[#Scripts Frameworks]]: [[#File Framework Hashes]], [[#File Framework Extract Files]], [[#Notice Framework Intelligence]]
	- [[#Scripts Packages]]

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

### Intro to Frameworks
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

___
### Scripts
[[#Table of contents|Back to the top]]

*Investigate and correlate events*

[Learn Zeek scripting](https://try.bro.org/#/?example=hello)

| Type of script      | Location                               |
| ------------------- | -------------------------------------- |
| Base (do not touch) | `/opt/zeek/share/zeek/base`            |
| User                | `/opt/zeek/share/zeek/site`            |
| Policy              | `/opt/zeek/share/zeek/policy`          |
| Local*              | `/opt/zeek/share/zeek/site/local.zeek` |
\**typically used for local customizations and configurations specific to your deployment*

`.zeek` extension

`load @/script/path` or `load @script-name` in `local.zeek` file: load script

Example Zeek script "`dhcp-hostname.zeek`":
```Zeek
event dhcp_message (c: connection, is_orig: bool, msg: DHCP::Msg, options: DHCP::Options)
{
print options$host_name;
}
```
Lines 1, 2 and 4 are predefined in Zeek syntax, only addition is line 3 that tells Zeek to extract DHCP hostnames

Use the script: **`zeek -C -r sample.pcap dhcp-hostname.zeek`**

[Zeek Built-In Functions](https://docs.zeek.org/en/master/script-reference/scripts.html)
- /opt/zeek/share/zeek/base/bif
- /opt/zeek/share/zeek/base/bif/plugins
- /opt/zeek/share/zeek/base/protocols

#### Selecting info

```Zeek
event new_connection(c: connection)
{
	print c;
}
```
*will print all info about connections*

```Zeek
event new_connection(c: connection)
{
	print ("###########################################################");
	print ("");
	print ("New Connection Found!");
	print ("");
	print fmt ("Source Host: %s # %s --->", c$id$orig_h, c$id$orig_p);
	print fmt ("Destination Host: resp: %s # %s <---", c$id$resp_h, c$id$resp_p);
	print ("");
}

# %s: Identifies string output for the source.
# c$id: Source reference field for the identifier.
```
*will print selected info about connections in formatted and more readable way*

NB: the names `orig_h`, `orig_p`, etc. can be found by zeeking the .pcap or in the output of the previous script

#### Scripts and Signatures

```Zeek
event signature_match (state: signature_state, msg: string, data: string)
{
if (state$sig_id == "ftp-admin")
    {
    print ("Signature hit! --> #FTP-Admin ");
    }
}
```
*uses the event* `signature_match`*combined with the signature* `ftp-admin.sig` *to check if there are matches*

Execute using this line: **`zeek -C -r ftp.pcap -s ftp-admin.sig 201.zeek`**

[More about events](https://docs.zeek.org/en/master/scripts/base/bif/event.bif.zeek.html)

Load Local Scripts: `zeek -C -r sample.pcap local`

Load Specific Scripts: `zeek -C -r ftp.pcap /opt/zeek/share/zeek/policy/protocols/ftp/detect-bruteforcing.zeek`

___
### Scripts | Frameworks
[[#Table of contents|Back to the top]]

#### File Framework | Hashes

Majority of frameworks meant to be used in scripting, not directly in CLI.

Calling a specific framework: `load @ $PATH/base/frameworks/framework-name`

```Bash
cat /opt/zeek/share/zeek/policy/frameworks/files/hash-all-files.zeek 
```

```Zeek
# Enable MD5, SHA1 and SHA256 hashing for all files.

@load base/files/hash
event file_new(f: fa_file)
	{
	Files::add_analyzer(f, Files::ANALYZER_MD5);
	Files::add_analyzer(f, Files::ANALYZER_SHA1);
	Files::add_analyzer(f, Files::ANALYZER_SHA256);
	}
```

Used to hash .pcap files

#### File Framework | Extract Files

```Bash
zeek -C -r case1.pcap /opt/zeek/share/zeek/policy/frameworks/files/extract-all-files.zeek
```

**`file * | nl`**: show more info on each file

Name of extracted file
- **`extract`**
- **`ts`** -- timestamp
- **`protocol`** -- source
- **`conn_uids`** -- connection id
	- *Example*: extract-1561667874.743959-HTTP-Fpgan59p6uvNzLFja

Investigate further on a particular conn_uid across all available logs
```Bash
grep -rin CZruIO2cqspVhLuAO9 * | column -t | nl | less -S
```

#### Notice Framework | Intelligence
*process, correlate, identify*

`/opt/zeek/intel/zeek_intel.txt`

1. Source file (`zeek_intel.txt`) has to be **tab-delimited**
2. **Adding lines** to it doesn't require redeploying (deleting lines does)

*Example* of a line inside `zeek_intel.txt`
```
smart-fax.com	Intel::DOMAIN	zeek-intel-test	Zeek-Intelligence-Framework-Test
```

Zeek script using intel
```Zeek
# Load intelligence framework!
@load policy/frameworks/intel/seen
@load policy/frameworks/intel/do_notice
redef Intel::read_files += { "/opt/zeek/intel/zeek_intel.txt" };
```
*will use* `zeek_intel.txt` *as intel source*

Output of zeek: `intel.log`

___
### Scripts | Packages
[[#Table of contents|Back to the top]]

