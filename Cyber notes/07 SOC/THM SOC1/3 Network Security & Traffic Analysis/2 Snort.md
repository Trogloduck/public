### Table of contents
- [[#Intro]]
- [[#Snort]]
- [[#Sniffer]]
- [[#Packet Logger]]
- [[#IDS/IPS]]
- [[#PCAP Investigation]]
- [[#Rule Structure]]
- [[#Operation Logic]]: [[#`snort.conf`]]

___
### Intro
[[#Table of contents|Back to the top]]

**IDS** -- Network Intrusion Detection System: passive, ***generates alerts***
- **NIDS** -- **Network** Intrusion Detection System: investigate traffic on ***network***
- **HIDS** -- **Host-based** Intrusion Detection System: traffic on single ***endpoint***

**IPS** -- Network Intrusion Prevention System: active, ***terminates connections***
- **NIPS** -- **Network** Intrusion Prevention System: protect network, terminate suspicious connections
- **Behavior-based** Intrusion Prevention System $\rightarrow$ **NBA** -- Network Behavior Analysis: require training period (***baselining***) to establish normal traffic
- **WIPS** -- **Wireless** Intrusion Prevention System
- **HIPS** -- **Host-based** Intrusion Prevention System

Detection/Prevention Techniques
- **Signature-based**: identify known threat's pattern
- **Behavior-based**: identify abnormal pattern (can identify unknown threats)
- **Policy-based**: detect policy violations

___
### Snort
[[#Table of contents|Back to the top]]

*Open-source, rule-based NIDS/NIPS*

3 main use models
- **Sniffer**: read IP packets
- **Packet Logger**: log IP packets
- **NIDS/NIPS**: log/drop suspicious packets according to rules

`snort -V`: Snort version

`snort -c /etc/snort/snort.conf -T`: **T**est **c**onfig file

Config file: rules, plugins, detection mechanisms, default actions, output settings; multiple config files for different purposes, run one at a time

___
### Sniffer
[[#Table of contents|Back to the top]]

`-v`: verbose
`-d`: packet **d**ata (payload)
`-e`: link-layer (TCP/IP/UDP/ICMP) headers
`-X`: HEX packet details
`-i`: network **i**nterface to sniff
Ex: `sudo snort -v -i eth0`

___
### Packet Logger
[[#Table of contents|Back to the top]]

`-l`: logger mode, default output folder: `/var/log/snort`
`-K ASCII`: log in ASCII format
`-r`: read logs (like sniffer)
`-n`: number of packets

Whoever creates file becomes owner $\rightarrow$ `sudo snort` $\Rightarrow$ root owns log file
$\Rightarrow$ always `sudo` to examine logs
$\Rightarrow$ `sudo chown [username] [file] / -R [directory]`: change ownership of log file/directory

ASCII can be read in text editor

Binary file can be read with the following methods
- `sudo snort -r snort.log.1638459842`
- `sudo tcpdump -r snort.log.1638459842 -ntc 10`
- Wireshark

**[BPF](https://biot.com/capstats/bpf.html)**: filter results
Ex: `snort -r snort.log.1640048004 -X  port 80`
`port 80` is the BPF

___
### IDS/IPS
[[#Table of contents|Back to the top]]

Manage traffic according to user-defined rules

`-c`: config file
`-T`: testing config file
`-N`: disable logging
`-D`: background mode, used for automation
`-A`: alert modes (specify amount of information to display about alerts)
- `full` (default): all possible information
- `fast`: message, timestamp, source-destination IP, port numbers
- `console`: fast style alert on console screen
- `cmg`: console message generator style, basic header details, hex and text format payload
- `none`: no alerting

Pre-defined ICMP rule: `alert icmp any any <> any any  (msg: "ICMP Packet Found"; sid: 100001; rev:1;)`
*alerts ICMP packets, any direction, located @ /etc/snort/rules/local.rules*

- Test config file: `sudo snort -c /etc/snort/snort.conf -T`
- Disable logging: `sudo snort -c /etc/snort/snort.conf -N`
- Drop packets: `-Q --daq afpacket`
- ...

Run snort with rule, without config file: `sudo snort -c /etc/snort/rules/local.rules -A console`

___
### PCAP Investigation
[[#Table of contents|Back to the top]]

`snort -r pcap_file.pcap`
`--pcap-list="item1.pcap item2.pcap"`
`--pcap-show`

___
### Rule Structure
[[#Table of contents|Back to the top]]

![[Pasted image 20250415142338.png]]

#### Action
	- `alert`: generate alert and log packet
	- `log`
	- `drop`: block and log
	- `reject`: block, log, terminate packet session
- Protocol: IP, TCP, UDP, ICMP, can detect other protocols using port numbers and options (Ex: FTP can be investigated by investigating TCP on port 21)

#### IP
	- Filtering: `alert icmp 192.168.1.56 any <> any any  (msg: "ICMP Packet From "; sid: 100001; rev:1;)`
	  - Range: `192.168.1.0/24`
	- Multiple ranges: `[192.168.1.0/24, 10.1.1.0/24]`
	- Exclude: `!192.168.1.0/24` ("!" -- negation operator)

#### Ports
	- Filtering: `alert tcp any any <> any 21  (msg: "FTP Port 21 Command Activity Detected"; sid: 100001; rev:1;)`
	- Range
		- Type 1: `1:1024`
		- Type 2: `:1024`
		- Type 3: `1025:`
		- Type 4: `[21,23]` -- list, not a range $\rightarrow$ possible to include ranges within lists
	- Exclude: `!21`

#### Direction
`->`: source to destination
`<>`: bidirectional
No `<-` operator...

#### Options
- General
- Payload: related to payload $\rightarrow$ payload patterns
- Non-Payload: specific patterns, network issues

**General**
- `msg: "message displayed if rule triggered"`
- `sid`: Snort rule ID
	- <100: reserved rules
	- 100-999: rules came with the build
	- >= 1 000 000: user created rules
- `reference:cve,CVE-XXXX`: could be CVE or other reference
- `rev`: analysts keep rule history, rev indicates # of revisions

**Payload**
- `content:"to be matched"`: like grep, case sensitive
- `nocase`: disables case sensitivity
- `fast_pattern`: when using multiple `content` options, prioritizes the directly preceding option

**Non-Payload**
- `id`: filter IP id field
- `flags`: TCP flags
	- `F`: FIN
	- `S`: SYN
	- `R`: RST
	- `P`: PSH
	- `A`: ACK
	- `U`: URG
- `dsize`: packet payload size
	- `dsize:min<>max`
	- `dsize:>min`
	- `dsize:<max`
- `sameip`: filter for IP duplicates

Edit local rules: `sudo gedit /etc/snort/rules/local.rules`

Test local rule against .pcap: `snort -c local.rules -A full -l . -r task9.pcap`

___
### Operation Logic
[[#Table of contents|Back to the top]]

Main components:
- **Packet Decoder**: collect, prepare packets for pre-processing
- **Pre-processors**: arranges, modifies packets for detection engine
- **Detection Engine**: primary component, dissect, analyze packets, apply rules
- **Logging and Alerting**
- **Outputs and Plugins**

Types of rules
- **Community**
- **Registered**: get subscriber rules 30 days after subscribers
- **Subscriber (Paid)**: updated 2x/week

https://www.snort.org/downloads

To use community/paid rules, indicate them in the snort.conf file

#### `snort.conf`

`sudo gedit /etc/snort/snort.conf`

`#` comments a line $\rightarrow$ uncomment line to activate operator

**Step #1: Set the network variables.**
`HOME_NET`: where we are protecting
`EXTERNAL_NET`: `any` or `!$HOME_NET`
`RULE_PATH`: hardcoded rule path (etc/snort/rules)
`SO_RULE_PATH`: come with registered and subscriber rules ($RULE_PATH/so_rules)
`PREPROC_RULE_PATH`: come with registered and subscriber rules ($RULE_PATH/plugin_rules)

**Step #2: Configure the decoder.**
`#config daq`: IPS mode selection
`#config daq_mode`: activate inline mode
`#config logdir`: hardcoded default log path (/var/logs/snort)

DAQ -- Data Acquisition modules: specific libraries used for packet I/O (Input/Output)

DAQ modules
- pcap (default): sniffer
- afpacket (inline): IPS mode
- ipq: inline on Linux, using Netfilter, replaces snort_inline patch
- nfq: inline mode on Linux
- ipfw: inline on Open-/Free-BSD
- dump: testing mode of inline and normalization

**Step #6: Configure output plugins**
Output of IDS/IPS (logging, alerting format details)

**Step #7: Customise your ruleset**
`# site specific rules`: hardcoded local / user rules path (includes $RULE_PATH/local.rule)
`#include $RULE_PATH`: hardcoded default/downloaded rules path (include $RULE_PATH/rulename)

___
[[Snort Cheatsheet.pdf]]