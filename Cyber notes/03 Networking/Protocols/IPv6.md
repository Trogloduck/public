< [[public/Cyber notes/03 Networking/Protocols/IP]]

128 bits instead of 32 ([[public/Cyber notes/03 Networking/Protocols/IPv4]])
--> can sustain $2^{128}$ IP addresses

IPv6 improvements
- Simplified header format
- More useful data
- Hierarchical network architecture
- Automatic address configuration
- No need for [[NAT]]

Header fields
- **Version** (4 bits: `0110`)
- **Traffic class** (8 bits) Allows packet prioritization
- **Flow label** (20 bits) allows to specify that all packets with same flow label should be processed in same way
- **Length of payload** (16 bits)
- **Next header** (8 bits) Indicates type of data carried by packet
- **Hop limit** (8 bits) represents the TTL
- **Source address**
- **Destination address**

![[Pasted image 20240902163107.png#center]]

