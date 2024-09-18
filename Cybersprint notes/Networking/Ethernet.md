< [[04 Networking]], < [[2. Data link]] and [[1. Physical]]

*Networking technology that defines protocols for data transmission over local area networks (LANs), involving physical cabling and hardware components to enable communication between devices*

Ethernet [[Frame]]:

| Preamble | Destination address | Source address | Type    | Data              | Frame check |
| -------- | ------------------- | -------------- | ------- | ----------------- | ----------- |
| 8 bytes  | 6 bytes             | 6 bytes        | 2 bytes | 46 to 1 500 bytes | 4 bytes     |
- **Preamble**: SFD (Start Frame Delimiter), synchronizes sender with receiver
- **Destination MAC address**: physical identifier of recipient
- **Source MAC address**: physical identifier of source
- **Type**: identifying protocol of previous source
- **Data**: data itself
- **Frame check**: FCS (Frame Check Sequence), detect frame errors and terminate frame


**[[Switch]]**'s two main methods to ***transfer frames*** to associated port:
1. **Cut-Through Method**:
    - ***Fast-Forward Variant***:
        - Switch starts sending frame to destination as ***soon*** as it reads destination address
        - ***No*** frame ***error check*** --> very fast
	- ***Fragment-Free Variant***:
        - Switch ***waits*** to read first ***64 bytes*** of frame before deciding where to send
	        - allows to ***check*** for small ***errors*** at start of frame
        - Compromise between speed and error checking
2. **Store and Forward Method**:
    - Switch ***waits*** until received ***entire*** frame and stores it in memory
    - ***Checks*** frame for ***errors*** using ***CRC*** (Cyclic Redundancy Check) by examining end of frame ("frame tail")
	    - error-free --> switch forwards to appropriate port
    - Slower than cut-through but ensures only valid data is sent

**[[Switch]]** types of ***buffers***:
- **Port-based**: frames stored in queues associated with each inbound and outbound port, data transmitted as soon as port becomes available
- **Shared memory**: single memory holds all frames and destination port dynamically allocated

**[[ARP]] request** ethernet frame **headers**:
- **Broadcast** MAC address allowing *everyone* to respond
- **Source** MAC address of the *sending* machine
- Frame **type**: *0x806* for ARP requests
	
	--> Display mapping table:
	- `show ip arp` on Cisco appliances
	- `arp -a` on Windows
	- `ip neigh` or `arp -n` on Linux

***ARP spoofing***: often used to facilitate other types of attack
- ***DoS*** (Denial of Service): use ARP spoofing to link multiple IP to a single target MAC (overloading traffic)
- ***Session hijacking***: ARP spoofing used to steal credentials
- ***Man-in-the-middle*** (MITM): ARP spoofing to intercept and modify traffic
