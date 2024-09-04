Internet Protocol address, used to identify device on network, can change, referred to as logical identifier

[[IP]] addresses follow sets of standardized rules called protocols to allow them to work with each other

IPv6 can sustain way more IP addresses than IPv4 (2^128 vs 2^32)

The protocol:
- connectionless: does not make connection with destination before sending packet
- does not allow to follow packets --> no receipt acknowledgement 
- independent of medium on which it is used but adapts  size of packets
- IP header: IP addresses of source and destination

Types of IP: 
- [[IPv4]]
- [[IPv6]]


IP \* subnet mask = network IP (in binary):
(the multiplication is called "ANDING", why? nobody knows)

Ex:

|                       | Decimal       | Binary                                        |
| --------------------- | ------------- | --------------------------------------------- |
| **IP Address**        | 192.10.10.33  | 1100 0000 . 0110 0100 . 0000 1010 . 0010 0001 |
| **Subnet Mask**       | 255.255.255.0 | 1111 1111 . 1111 1111 . 1111 1111 . 0000 0000 |
| *Multiply bit by bit* |               |                                               |
| **Network IP**        | 192.10.10.0   | 1100 0000 . 0110 0100 . 0000 1010 . 0000 0000 |

