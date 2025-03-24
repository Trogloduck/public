### Table of contents
- [[#1. Reconnaissance]]
- [[#2. Weaponization]]
- [[#3. Delivery]]
- [[#4. Exploitation]]
- [[#5. Installation]]
- [[#6. Command & Control (C2)]]
- [[#7. Actions on Objectives]]

___
![[Pasted image 20250322110855.png|500]]

___
### 1. Reconnaissance
[[#Table of contents|Back to the top]]

- **[theHarvester](https://github.com/laramies/theHarvester)**: gather emails, names, subdomains, IPs, URLs from public data sources 
- **[Hunter.io](https://hunter.io/)**: email hunting tool - contact information associated with domain
- **[OSINT Framework](https://osintframework.com/)**: collection of OSINT tools based on various categories
- Social media

___
### 2. Weaponization
[[#Table of contents|Back to the top]]

*Combine **malware** and **exploit** into **payload***

- **Malware**: software designed to damage, disrupt, gain unauthorized access
- **Exploit**: code that takes advantage of vulnerability in application/system
- **Payload**: code attacker runs on system

[Intro to Macros and VBA For Script Kiddies](https://www.trustedsec.com/blog/intro-to-macros-and-vba-for-script-kiddies/)

___
### 3. Delivery
[[#Table of contents|Back to the top]]

- **Phishing**
- **USB drives** distributed in public
- **Watering hole attack**
	1. Determine which websites target visits frequently
	2. Infect website/s with malware
	3. / Incite victim to visit website through compromised website's communication channel

___
### 4. Exploitation
[[#Table of contents|Back to the top]]

- **Victim** triggers exploit by opening email **attachment** / clicking on malicious **link**
- **Zero-day** exploit
- Exploit **software**, **hardware**, **human vulnerabilities** 
- **Attacker** triggers exploit for **server-based** vulnerabilities

___
### 5. Installation
[[#Table of contents|Back to the top]]

**Persistent backdoor**: maintain access to target despite initial access removed / system patched

- **Web shell**
	- Installed on **webserver**
	- Malicious script written in **web development programming languages** (ASP, PHP, JSP, ...)
	- Simplicity and file formatting (.php, .asp, .aspx, .jsp, etc.) $\rightarrow$ **difficult to detect**, might be classified as benign. Read [more](https://www.microsoft.com/security/blog/2021/02/11/web-shell-attacks-continue-to-rise/)
- **Backdoor**
	- Installed on victim's machine
	- **[Meterpreter](https://www.offensive-security.com/metasploit-unleashed/meterpreter-backdoor/)**: Metasploit Framework payload, interactive shell from which attacker can interact with victim's machine remotely and execute malicious code, can be used to install backdoor
- **Windows Service Manipulation -- [MITRE ATT&CK T1543.003](https://attack.mitre.org/techniques/T1543/003/)**
	- **Creating/modifying Windows services**: execute malicious payloads persistently
	- **Tools Used**:
	    - `sc.exe` (Create, Start, Stop, Query, or Delete services)
	    - `Reg` (Modify service configurations)        
	- **Masquerading**: use service names resembling OS/legitimate software to evade detection
- **Run Keys / Startup Folder -- [MITRE ATT&CK T1547.001](https://attack.mitre.org/techniques/T1547/001/)**
	- **Method**: Adding malicious payload to:
	    - **Registry Run Keys** $\rightarrow$ Executes on user login
	    - **Startup Folder** $\rightarrow$ System-wide or per-user execution
	- **Persistence**: payload runs automatically at each login

**Timestomping -- [MITRE ATT&CK T1070.006](https://attack.mitre.org/techniques/T1070/006/)**: modifying timestamps to cover tracks

___
### 6. Command & Control (C2)
[[#Table of contents|Back to the top]]

**C&C / C2 Beaconing**: communication between C2 and malware on infected host

IRC (Internet Relay Chat) is obsolete for this purpose

Most commonly used channels
- **HTTP/S** (port 80/443): blends malicious traffic with legitimate one
- **DNS Tunneling**: compromised machine makes constant DNS request to DNS server owned by attacker

___
### 7. Actions on Objectives
[[#Table of contents|Back to the top]]

- Collect credentials
- Privilege escalation
- Internal reconnaissance
- Lateral movement through company's environment
- Collect, exfiltrate sensitive data
- Deleting backups and shadow copies
- Overwrite/corrupt data