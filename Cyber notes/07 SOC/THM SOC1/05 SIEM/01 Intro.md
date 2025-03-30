### Table of contents
- [[#Network Visibility through SIEM]]
- [[#Log Sources & Ingestion]]
- [[#Capabilities]]
- [[#Analyzing Logs and Alerts]]
	- [[#Dashboard]]
	- [[#Correlation Rules]]
	- [[#Alert Investigation]]

___
*Security Information and Event Management System*

___
### Network Visibility through SIEM
[[#Table of contents|Back to the top]]


![[Pasted image 20250330171443.png#center|500]]

Several log sources: Sysmon, Windows Event Logs on Windows endpoints, ...

**Log Sources**
1. **Host-Centric**: events occurred within/related to host
2. **Network-Centric**: hosts communicate with each other / access internet -- SSH, VPN, HTTP/S, FTP, ...

![[Pasted image 20250330171921.png#center|500]]

___
### Log Sources & Ingestion
[[#Table of contents|Back to the top]]

#### Sources

**Common devices found in a network**

- Windows Machine
	$\rightarrow$ Event Viewer: unique ID for each activity
- Linux Workstation
	$\rightarrow$ `/var/log/httpd`: HTTP Request/Response/Error
	$\rightarrow$ `/var/log/cron`: cron jobs
	$\rightarrow$  `/var/log/auth.log` & `/var/log/secure`: authentication
	$\rightarrow$  `/var/log/kern`: kernel
- Web Server -- Linux (apache)
	$\rightarrow$ `/var/log/apache` or `/var/log/httpd`

#### Ingestion

![[Pasted image 20250330172732.png#center|500]]

Methods
1. **Agent/Forwarder**: installed on endpoint, capture important logs and send to SIEM server
2. **Syslog**: protocol, collect data, send in real-time to centralized destination
3. **Manual Upload**: ingest, normalize data manually offline for quick analysis
4. **Port-Forwarding**: SIEM configured to listen on certain port, endpoint forwards data to SIEM

___
### Capabilities
[[#Table of contents|Back to the top]]

- **Correlation** between events from different log sources
- **Visibility** on Host-centric and Network-centric activities
- **Investigate** latest threats, **respond**
- **Hunt** for threats not detected by rules in place

SOC Analyst Responsibilities
- **Monitoring**, **Investigating**
- **False positives** (identify)
- **Tuning** noise causing / false-positive inducing **Rules**
- **Reporting**, **Compliance**
- **Blind spots** in network visibility (identify and cover)

___
### Analyzing Logs and Alerts
[[#Table of contents|Back to the top]]

#### Dashboard

- Alert Highlights
- System Notification
- Health Alert
- Failed Login Attempts List
- Events Ingested Count
- Rules triggered
- Top Domains Visited

#### Correlation Rules

*Examples*
- User gets 5 failed Login Attempts in 10 seconds $\rightarrow$ Alert  `Multiple Failed Login Attempts`
- Login is successful after multiple failed login attempts $\rightarrow$ Alert `Successful Login After multiple Login Attempts`
- User plugs in USB $\rightarrow$ Alert `USB Plugged In` (depends on company policy)
- Outbound traffic > 25 MB $\rightarrow$ Alert `Potential Data Exfiltration Attempt` (depends on company policy)

How rules are created

Use-Case 1
**Technique**: Adversary deletes logs to remove tracks
**Event ID**: 104 (attempt to clear event logs)
**Rule**: If Log source is WinEventLog AND EventID is 104 $\rightarrow$ Trigger `Event Log` alert

Use-Case2
**Technique**: Adversary uses command `whoami`after exploitation/ privilege exploitation
**Event ID**: 4688 (Process Execution); **NewProcessName** contains `whoami`
**Rule**: If Log Source is WinEventLog AND EventCode is 4688, and NewProcessName contains whoami $\rightarrow$ Trigger `WHOAMI command Execution DETECTED` alert

#### Alert Investigation

Investigate to determine if true or false positive

$\rightarrow$ Alert is False Alarm $\rightarrow$ tuning rule to avoid similar False positives

$\rightarrow$ Alert is True Positive $\rightarrow$ further investigation  
$\rightarrow$ Contact asset owner to inquire about activity
$\rightarrow$ Suspicious activity is confirmed $\rightarrow$ Isolate infected host
$\rightarrow$ Block suspicious IP