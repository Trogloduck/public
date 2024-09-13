< [[IP]]

32 bits
--> can sustain $2^{32}$ IP addresses (4 294 967 296)
--> [[IPv6]] to respond limitation

IPv4 packet headers:

- **Version** (4 Bits): version of IP used (in the case of IPv4: `0100`)
- **Different service** (8 Bits): gives priority to certain packets
- **Time-To-Live (TTL)** (8 Bits): limits lifetime of packet; decreases by 1 each time packet is processes by router
- **Protocol** (8 Bits): protocol used by previous layer
- **Source IP address**: IP address of sending machine
- **Destination IP address**: IP address of destination machine

# ajouter une image d'un frame IPv4

[[Classes of IPv4]]: 

| Class | Description                         | Range of IP        |
| ----- | ----------------------------------- | ------------------ |
| A     | Networks with large number of hosts | **\[0, 127]**      |
| B     | Medium to large networks            | **\[128, 191]**    |
| C     | Small LANs                          | **\[192, 223]**    |
| D     | Multicasting                        | **\[224, 239]**    |
| E     | Research/experimental use           | **\[240, 255]**    |
