https://tryhackme.com/room/nmap01

### Table of contents
- [[#Intro]]
- [[#Subnetting]]
- [[#Enumerating Targets]]
- [[#Discovering Live Hosts]]
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

Discover information about group of hosts / subnet --> connect to same subnet, scanner rely on ARP (Address Resolution Protocol) queries, aiming hardware address (MAC)

If on different subnet from target, ARP queries won't reach

___
### Enumerating Targets
[[#Table of contents|Back to the top]]

Target specification
- **List:** `MACHINE_IP scanme.nmap.org example.com`
- **Range:** `10.11.12.15-20`
- **Subnet:** `MACHINE_IP/30`
- **File:** `nmap -iL list_of_hosts.txt`

Option `-sL`: checks list of hosts without scanning, reverse DNS resolution attempt to obtain names (no DNS: `-n`)

___
### Discovering Live Hosts
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
