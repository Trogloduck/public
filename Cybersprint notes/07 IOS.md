***IOS***: Internetwork Operating System, found on routers and switches

Access:
- Console: physical connection
- SSH: remote connection
- Telnet: unsecure, passwords in plain text
- AUX: using telephone connection

Command modes:

| Name                    | Prompt         | Accessed through | Access command     | Ability                                               |
| ----------------------- | -------------- | ---------------- | ------------------ | ----------------------------------------------------- |
| User                    | >              |                  |                    | limited monitoring, prevents configuration changes    |
| Privileged              | #              | User             | enable             | maintenance, configuration operations on router       |
| Configuration           | (config)#      | Privileged       | configure-terminal | modify device configuration                           |
| Line configuration      | (config-line)# | Configuration    | line               | modify configuration of console access, SSH or Telnet |
| Interface configuration | (config-if)#   | Configuration    | interface          | modify configuration network interfaces               |

Composition of an IOS command:
![Prompt> commande arguments](https://camo.githubusercontent.com/29df52b6264b3433e9e85f8286000f14715630515b2d04b4903a15ecca87dd50/68747470733a2f2f6d796265636f64652d66696c65732d70726f64756374696f6e2e73332d65752d776573742d312e616d617a6f6e6177732e636f6d2f66353363626133622d336532612d346331662d386435302d3335323838396432633162662d636f6d6d616e64652e706e67)


Passwords setup to ensure security:

| Mode          | Setup through                            | command                                 |
| ------------- | ---------------------------------------- | --------------------------------------- |
| Privileged    | Global configuration                     | `enable secret`                         |
| User          | Online configuration (`line console 0`)  | `password`, deactivated with `no login` |
| Remote access | Vty configuration mode (`line vty 0 15`) | same as above                           |

Enable password *encryption*: global configuration mode --> `service password-encryption`

*Legal* message: inform of private nature of material --> banner displayed at each connection `banner word #<message>#`

***Interface***: junction between machine's hardware and network medium
Type of interface varies depending on:
- distance over which medium can transmit information
- environment of the media
- throughput
- cost of installation

***SVI*** (Switch Virtual Interface): remotely managing switch

SVI configuration: 
1. enter the *interface configuration* mode --> `interface vlan 1` (vlan 1 is a default name for SVI) from privileged execution mode
2. configure IP -->  `ip address <ip address> <mask>`
3. restart interface --> `no shutdown`
___
CISCO packets tracer
