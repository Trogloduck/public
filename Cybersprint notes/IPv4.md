Type of [[IP]]

32 bits
--> can sustain $2^{32}$ IP addresses (4 294 967 296)
--> [[IPv6]] to respond limitation

Uses [[NAT]]

IPv4 packet headers:

- **Version** (4 Bits): version of IP used (IPv**4** -- `0100`)
- **Different service** (8 Bits): gives priority to certain packets
- **Time-To-Live (TTL)** (8 Bits): limits lifetime of packet; decreases by 1 each time packet is processes by router
- **Protocol** (8 Bits): protocol used by previous layer
- **Source IP address**: IP address of sending machine
- **Destination IP address**: IP address of destination machine