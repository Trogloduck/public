< [[04 Networking]]

Computer composed of **[[IOS]]**, processor, RAM, ROM. 
***Connects networks*** and passes data between them, performs ***routing*** (creating a path for data packets to travel to their destination, using **[[IP]]**)

- **RAM**: store information quickly
- **Read-only memory**: data cannot be modified (except by Cisco of course)
- **Non-volatile RAM**: permanent storage for `startup-config` configuration file
- **Flash memory**: non-volatile memory containing system and log files
- **Advanced integration module**: used to offload processor from time consuming actions such as cryptography
___

***Configuration***:

- Enter interface ***configuration mode***
	`interface gigabitethernet 0/0`
- Configure ***network*** of interface
	`ip address 192.168.10.1 255.255.255.0`
- Configure ***default gateway***
	`ip default-gateway 192.168.10.50`
- Give ***description*** for interface
	`description Link to LAN-10`
- ***(Re)start*** interface
	`no shutdown`

***Check configuration***: 

- `show ip interface brief`: overview of interfaces
- `show ip route`: routing table
- `show interfaces`: interface statistics
- `show ip interface`: IPv4 statistics for interfaces
___

**Routing table**:
In ***local network***, before the IP and mask,
- `C` (Connected) indicates the network was ***discovered automatically***
- `L` (Local) indicates the network was ***manually configured***

On a ***remote network***,
- `S` for a ***static route***, `D` for ***Enhanced Interior Gateway Routing Protocol***, `O` for ***Open Shortest Path First***
- ***Destination Network***: IP, mask of destination
- ***Administrative distance***: measure of the trustworthiness of route (lower is better)
- ***Metric***: value used by routing protocols to determine cost of reaching destination, can represent hop count, bandwidth, delay, etc. Lower is better.
- ***Next leg***: IP address of next router/gateway where packets should be sent on their way to destination
- ***Route timestamp***: indicates when route was last maintained
- ***Exit interface***: interface to send the packet to for this route

