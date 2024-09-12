- [[#***Networking*** connecting things together]]
- [[#***Topology*** design of the network]]
- [[#Network protocols]]

***Offensive*** security: behaving like a hacker
***Defensive*** security: defending against hackers
___
##### ***Networking***: connecting things together

Internet: network of smaller networks, repository to store and share information
*Private* network < *public* network < Internet

Every machine on a network is called a host, 2 types of software on those hosts:
    • ***client***: request services
    • ***servers***: provide services

Peer-to-peer: network composed of hosts that are both client and server

3 main network components:
    •[[Physical]]: devices and physical connection
    • Services

A network uses [[IP]] and [[MAC]] to identify devices on it

ping uses ICMP (Internet Control Message Protocol) to assess performance of connection between 2 devices

**Know about *[[0. OSI]]* (frequent interview question)**

***LAN*** (Local Area Network – home/building) < ***MAN*** (Metropolitan Area Network – city-wide) < ***WAN*** (Wide Area Network – global or country-wide)
WLAN: Wireless LAN; SAN: Storage Area Network

Intranet: small network owned by an organization >< Extranet: allows communication with organization outside its LAN/MAN

Internet ***access***:
    • DSL: telephone network with DSL technology
    • Cable: direct connection to network through specific cable
    • Cellular: wireless telephone signal
    • Satellite: more useful in remote areas
    • Dial-up Internet access: low speed connection

Necessary ***qualities*** of a network:
    • Fault-tolerance: available even if a component fails
    • Scalability: easy to add new
    • Quality: good throughput
    • Security: confidentiality, integrity, authentication
___
##### ***Topology***: design of the network

***LAN***: Local Area Network

***Star*** topology: devices connected to central device (switch/hub)
Most common topology, more cabling needed, but more scalable (easy to add devices), more maintenance needed

***Bus*** topology: relies on a single connection (backbone cable)
Prone to becoming slow and bottlenecked because all information travels on the same cable
Difficult troubleshooting: difficult identification of device causing issue
Easier and most cost efficient

***Ring*** topology: devices are connected in a loop
Less dependency to hub/switch
The loop only works one way, a device will send its data prior to any other data it receives
Easy to troubleshoot
Information may have to travel through multiple devices before reaching intended device

Other examples of topology:
![[Pasted image 20240902163524.png]]

**[[Router]]**: connects networks and passes data between them, performs routing (creating a path for data packets to travel to their destination, using IP)
**[[Switches]]**: aggregates multiple devices within a network, the devices plug into a switch’s port, doesn’t perform routing, uses packet switching breaking down data into smaller more manageable chunks of data

Switches and routers can be used in the same network, increasing ***redundancy***, adding multiple paths for data to travel on

**[[Subnetting]]**: subdividing a network into smaller networks within itself

Host address: IP address of a device within a subnet
Ex: 192.168.1.100
Network address: IP address identifying the start of a network, used to identify network’s existence
Ex: 192.168.1.0
Default gateway: Special IP address assigned to device able to send information on another network (→ the router)
Ex: 192.168.1.1 or 192.168.1.254

*Subnet mask*: determines which part of the IP identifies the network
Ex: subnet mask of 255.255.255.0 with an IP address of 162.198.1.5 → network is 162.198.1, host is 5
255.255.255.0 can have 254 hosts (2^8 - 2)
255.255.0.0 can have 65 534 hosts (2^16 – 2)
___
##### Network protocols

**[[ARP]]**:
Wi-Fi box uses ARP to assign IP to my computer

**[[DHCP]]**:
Server uses DHCP to assign IP to Wi-Fi box

**[[Transport]] layer protocols**: TCP/UDP

***traceroute*** (tracert command) records path from source to destination and time (ms) at each hop
Number of routers: number of ‘hops’ data traveled from source to destination

