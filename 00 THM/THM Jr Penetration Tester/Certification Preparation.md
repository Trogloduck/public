| Topic               | %   |
| ------------------- | --- |
| 1. Web App          | 40  |
| 2. Network Sec      | 36  |
| 3. Active Directory | 24  |
Success threshold: **75%**

- [ ] Have **ID** ready for verification


### Topics details

1. Recon & Enum
	- **Basic Network Recon:** identify IP ranges, subnets, subdomain enum, list publicly exposed services, ...
	- **Active Info Gathering:** nmap (open ports, OS, running services TCP/UDP)
	- **Tools and Commands:** nmap, dig, whois, banner grabbing, DNS analysis, service enum, ***build attack surface***

2. Web App
	- **OWASP Top 10:** SQL injection, XSS, IDOR, SSRF, ...
	- **Manual Testing:** Burp, browser-based, exploit input validation flaws, broken access control, file upload issues, ...
	- **Bypassing:** bypass basic client-side controls (JS restrictions, UI-based limitations, ...)

3. Network
	- **Service Enum & Exploit:** SMB, RDP, FTP, SSH, SNMP to identify vulnerabilities
	- **Password Attacks, Misconfig Abuse** 
	- **Local Privilege Escalation** (Linux & Windows)
	- **Traffic Inspection, Network Defense Awareness:** sniffing, MITM, capture credentials, firewall evasion strategies

4. AD
	- **Domain & Object Enum:** BloodHound, built-in Windows commands to map out AD structures, relationships, permissions
	- **Attack Paths:** asrep roasting, kerberoasting, credential harvesting, abusing outdated software, privilege escalation
	- **Pivoting, Lateral Movement:** identify trust relationships

5. Exploit and Post-exploit
	- **Privilege Escalation:** SUID, kernel exploit, service misconfigurations (Linux & Windows)
	- **Post-Exploitation:** host recon, user enum, credential dumping, persistence

6. Reporting & Time Management
	- **Clear Technical Report:** 
		- **Concise**
		- **Actionable** vulnerability descriptions
		- **Impact** assessments
		- **Reproduction** steps
		- Recommended **mitigations**
	- **Time and Tasks Prioritization:** 48h windows, identify high-value targets early, allocate time wisely
	- **Note-Taking, Communication:** thorough, clear notes, provide logical attack path narrative communicating risk to technical and ***non-technical*** stakeholders