Type of [[IP]]

128 bits instead of 32 ([[IPv4]])
--> can sustain $2^{128}$ IP addresses

- simplified header format
- more useful data
- hierarchical network architecture
- automatic address configuration
- no need for NAT

Headers:

- **Version** (4 bits) (6 -- `0110`)
- **Traffic class** (8 bits) allows to prioritize the packet
- **Flow label** (20 bits) allows to specify that all packets with same flow label should be processed in same way
- **Length of payload** (16 bits)
- **Next header** (8 bits) indicates type of data
- **Hop limit** (8 bits) represents TTL
- **Source address**
- **Destination address**

![[Pasted image 20240902163107.png]]

