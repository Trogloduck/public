https://tryhackme.com/room/nmap01

### Table of contents
- [[#Intro]]
- [[#Subnetting]]
- [[#Enumerating Targets]]
- [[#Protocols]]
	- [[#ARP]]
	- [[#ICMP]]
	- [[#TCP/UDP]]
- 

___
### Intro
[[#Table of contents|Back to the top]]
*Network Mapper* 

- What systems are up
- What services are running on them

Common steps in nmap scan
![[Pasted image 20251212160635.png|400]]


___
### [[Subnetting]]
[[#Table of contents|Back to the top]]

Discover information about group of hosts / subnet --> connect to same subnet, scanner rely on **[[ARP]]** (Address Resolution Protocol) queries, aiming hardware address (MAC)

If on different subnet from target, ARP queries won't reach

___
### Enumerating Targets
[[#Table of contents|Back to the top]]

Target specification
- **List:** `MACHINE_IP scanme.nmap.org example.com`
- **Range:** `10.11.12.15-20`
- **Subnet:** `MACHINE_IP/30`
- **File:** `nmap -iL list_of_hosts.txt`

***Option*** `-sL`: checks list of hosts without scanning, reverse DNS resolution attempt to obtain names (no DNS: `-n`)

___
### Protocols

- **ARP:** get MAC address from specific IP
- **ICMP:** ping (type 8 (echo), type 0 (echo reply))
- **TCP/UDP:** useful if ICMP blocked

#### ARP
[[#Table of contents|Back to the top]]

Default nmap approaches
- **Privileged user** tries to scan
	- on **local network** (Ethernet): ARP requests
	- **outside** local network: ICMP echo requests, TCP ACK to port 80, TCP SYN to port 443, ICMP timestamp request
- **Unprivileged user** tries to scan **outside** local network: TCP 3-way handshake (SYN to ports 80 and 443)

By default, nmap uses ping to find live hosts, then scans live hosts only

***Option*** to discover live hosts without port scanning: `-sn`
ARP scan: `-PR`

Tool for ARP scans: `arp-scan`
`apt install arp-scan`, `arp-scan --localnet`/`arp-scan -l`

#### ICMP 
[[#Table of contents|Back to the top]]

`-PE`: ICMP **E**cho request (ping)

`-PP`: ICMP timestam**p** request (type 13, response -- type 14)

`-PM`: ICMP **M**ask query (type 17, response -- type 18)

#### TCP/UDP 
[[#Table of contents|Back to the top]]

- **TCP SYN Ping** -- `-PS<port_number>`
Send packet with SYN flag to TCP port (80 by default)
	> Open port replies with SYN/ACK
	> Closed port replies with RST

Examples: `-PS21`, `-PS21-25`, `-PS80,443,8080`

- **TCP ACK Ping** -- `-PA<port_number>`
Send packet with ACK flag to TCP port, should get a RST response (because no established connection)

- **UDP Ping** -- `-PU<port_number>`
No response expected from open ports, closed ports reply with ICMP port unreachable packet

- **`masscan`** -- `-p`
Similar approach but can be noisy because sends a lot of packets
`apt install masscan`

___
### Reverse DNS Lookup
[[#Table of contents|Back to the top]]

Default

Deactivate: `-n`

`-R`: query DNS server for offline hosts too

`-dns-servers DNS_SERVER`: request specific DNS server