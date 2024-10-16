< [[04 Networking]]

***IOS***: Internetwork Operating System, Cisco's proprietary operating system used on its routers and network switches, providing routing, switching, network security, and management through command-line interface

***Access***:
- ***Console***: *physical* connection
- ***SSH***: *remote* connection
- ***Telnet***: *unsecure*, passwords in plain text
- ***AUX***: using *telephone* connection

**Command modes**:

| Name                          | Prompt         | Accessed through | Access command       | Ability                                               |
| ----------------------------- | -------------- | ---------------- | -------------------- | ----------------------------------------------------- |
| ***User***                    | >              | (default)        |                      | limited monitoring, prevents configuration changes    |
| ***Privileged***              | #              | User             | `enable`             | maintenance, configuration operations on router       |
| ***Configuration***           | (config)#      | Privileged       | `configure-terminal` | modify device configuration                           |
| ***Line configuration***      | (config-line)# | Configuration    | `line`               | modify configuration of console access, SSH or Telnet |
| ***Interface configuration*** | (config-if)#   | Configuration    | `interface`          | modify configuration network interfaces               |

***IOS command*** components:
![[Cyber notes/images/ios.jpg#center| 650]]

**Passwords** setup to ensure security:

| Mode                | Setup through                               | command                                                                    |
| ------------------- | ------------------------------------------- | -------------------------------------------------------------------------- |
| ***Privileged***    | Global configuration (`configure-terminal`) | `enable secret <password>`                                                 |
| ***User***          | Online configuration (`line console 0`)     | `password <password>`, activated with `login`, deactivated with `no login` |
| ***Remote access*** | Vty configuration mode (`line vty 0 15`)    | same as ***User***                                                         |

Enable password ***encryption***: global configuration mode --> `service password-encryption`

***Legal*** message: inform of private nature of material --> *banner* displayed at each connection `banner word #<message>#`

***Interface***: junction between machine's hardware and network medium
Type of interface varies depending on:
- *distance* over which medium can transmit information
- *environment* of the media
- *throughput*
- *cost* of installation

***SVI*** (Switch Virtual Interface): remotely managing switch

SVI configuration: 
1. enter the *interface configuration* mode --> `interface vlan 1` (vlan 1 is a default name for SVI) from privileged execution mode
2. configure IP of default gateway -->  `ip address <ip address> <mask>`
3. restart interface --> `no shutdown`
___

CISCO packets tracer
