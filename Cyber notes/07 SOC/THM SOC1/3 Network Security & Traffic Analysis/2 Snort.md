### Table of contents
- [[#Intro]]
- [[#Snort]]
- [[#Sniffer]]
- [[#Packet Logger]]
- [[#IDS/IPS]]
- [[#PCAP Investigation]]
- [[#Rule Structure]]

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
