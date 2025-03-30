### Table of contents
- [[#Network Visibility through SIEM]]
- [[#Log Sources & Ingestion]]
- 

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
