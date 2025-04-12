### Table of contents
- [[#IDS/IPS]]
- [[#Snort]]
- 

___
### IDS/IPS
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

