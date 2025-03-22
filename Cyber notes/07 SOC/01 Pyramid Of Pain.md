### Table of contents
- [[#1. Hash Values]]
- [[#2. IP Address]]
- [[#3. Domain Names]]
- [[#4. Host Artifacts]]
- [[#5. Network Artifacts]]
- [[#6. Tools]]
- [[#7. TTPs -- Techniques, Tactics & Procedures]]

___
![[Pasted image 20250322102203.png|500]]
This pyramid ranges **indicators** from most easily **bypassable** to least easily (for an attacker): it's very easy to slightly modify a malware's code in order for it to have a completely different hash value while it's very hard to 

**[app.any.run](https://app.any.run)**: sandbox environment, detonate object and observe its activity, investigate links, ...

___
### 1. Hash Values
[[#Table of contents|Back to the top]]

MD5 is not secure, vulnerable to hash collision
Hash lookup: [VirusTotal](https://www.virustotal.com/gui/), [Metadefender Cloud - OPSWAT](https://metadefender.opswat.com/?lang=en)
```powershell
Get-FileHash PATH/TO/FILE -Algorithm MD5
```
```Shell
md5sum PATH/TO/FILE
```

___
### 2. IP Address
[[#Table of contents|Back to the top]]

Fast Flux: hiding behind compromised hosts used as proxies $\rightarrow$ harder to find malware's C2 (Command & Control server) 

Learn [more](https://unit42.paloaltonetworks.com/fast-flux-101/)

___
### 3. Domain Names
[[#Table of contents|Back to the top]]

- Typosquatting, Punycode
- Shorten URL
	- bit.ly
	- goo.gl
	- ow.ly
	- s.id
	- smarturl.it
	- tiny.pl
	- tinyurl.com
	- x.co
$\rightarrow$ use unshortener webapp to uncover original domain

___
### 4. Host Artifacts
[[#Table of contents|Back to the top]]
*Traces attackers leave on system: registry values, suspicious process execution, attack patterns or IOCs (Indicators of Compromise), files dropped by malicious applications, or anything exclusive to the current threat*

___
### 5. Network Artifacts
[[#Table of contents|Back to the top]]

- User-Agent string: request-header indicating user-agent originating request
- Detected by network monitoring tools: Wireshark, Snort
```Bash
tshark --Y http.request -T fields -e http.host -e http.user_agent -r analysis_file.pcap
```
*isolates user-agent field*

Research user-agent string

___
### 6. Tools
[[#Table of contents|Back to the top]]

Antivirus signatures, detection rules, and YARA rules

[MalwareBazaar](https://bazaar.abuse.ch/), [Malshare](https://malshare.com/): samples, malicious feeds, YARA results $\rightarrow$ threat hunting, incident response

[SOC Prime Threat Detection Marketplace](https://tdm.socprime.com/): detection rules shared by security professionals 

**Fuzzy hashing** -- **CPTH** (Context Triggered Piecewise Hashes): two similar inputs will generate two similar hash values $\rightarrow$ [SSDeep](https://ssdeep-project.github.io/ssdeep/index.html)

___
### 7. TTPs -- Techniques, Tactics & Procedures
[[#Table of contents|Back to the top]]

$\rightarrow$ **[MITRE ATT&CK](https://attack.mitre.org/)**
$\rightarrow$ [Advanced Persistent Threat (APT) Groups](https://docs.rapid7.com/insightidr/apt-groups/)