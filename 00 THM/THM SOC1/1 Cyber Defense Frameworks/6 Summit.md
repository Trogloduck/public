https://tryhackme.com/room/summit

1. `sample1.exe` -- **Hash**
	1. Analyze sample in Malware Sandbox
	2. Copy-paste **MD5** Hash in Manage Hashes

2. `sample2.exe` -- **IP**
	1. Analyze sample in Malware Sandbox
	2. Block IP address in **Firewall** Rule Manager (Egress, Any, IP, Deny)

3. `sample3.exe` -- **Domain Name**
	1. Analyze sample in Malware Sandbox
	2. Block domain in **DNS** Rule Manager

4. `sample4.exe` -- **Host Artifacts**
	1. Analyze sample in Malware Sandbox
	2. **Sigma** Rule Builder > Sysmon Event Logs > Registry Modifications > Enter information for "DisableRealTimeMonitoring" event (Defense Evasion)

5. `sample5.exe` -- **Network Artifacts**
	1. Inspect `outgoing_connections.log`
	2. Notice pattern: 97 bytes, every 30' on same IP and port
	3. **Sigma** Rule Builder > Sysmon Event Logs > Network Connections > Any, Any, 97, 1800, Command & Control

6. `sample6.exe` -- **Tools**
	1. Inspect `commands.log`
	2. Notice `%temp%\exfiltr8.log` being used to collect and exfiltrate data
	3. **Sigma** Rule Builder > Sysmon Event Logs > File Creation and Modification > `%temp%`, `exfiltr8.log`, Exfiltration