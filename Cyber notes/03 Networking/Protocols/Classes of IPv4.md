< [[public/Cyber notes/03 Networking/Protocols/IP]]

[[public/Cyber notes/03 Networking/Protocols/IPv4]] five classes: A, B, C, D, E
A, B, C used by majority of devices

Private addresses: within network
Loop addresses: network troubleshooting
___

| Class | Description                         | Range of IP     |
| ----- | ----------------------------------- | --------------- |
| **A** | Networks with large number of hosts | **\[0, 127]**   |
| **B** | Medium to large networks            | **\[128, 191]** |
| **C** | Small LANs                          | **\[192, 223]** |
| **D** | Multicasting                        | **\[224, 239]** |
| **E** | Research/experimental use           | **\[240, 255]** |
___

**Class A**: Public & Private IP Address Range

Networks with ***large number of hosts***
Up to 126 networks using the first octet for the network ID
1st bit in 1st octet always zero (<128), 24 remaining bits (3 octets) represent hosts ID --> ~17 million hosts per network
Class A network number values: **\[0, 127]**

- Public IP Range: 1.0.0.0 to 127.0.0.0
- Private IP Range: 10.0.0.0 to 10.255.255.255 (See Private IP 
- Subnet Mask: 255.0.0.0 (8 bits)
- Number of Networks: 126
- Number of Hosts per Network: 16 777 214
---

**Class B**: Public & Private IP Address Range

***Medium to large networks***
Up to 16 384 networks using first 2 octets for the network ID
First 2 bits in 1st octet always 1 0, remaining 6 bits, together with 2nd octet, complete network ID 16 bits in 3rd and 4th octets represent host ID --> 65 000 hosts per network
Class B network number values: **\[128, 191]**

- Public IP Range: 128.0.0.0 to 191.255.0.0
- Private IP Range: 172.16.0.0 to 172.31.255.255
- Subnet Mask: 255.255.0.0 (16 bits)
- Number of Networks: 16 382
- Number of Hosts per Network: 65 534
___

**Class C**: Public & Private IP Address Range

***Small LANs*** (local area networks)  
Up to ~2 million networks using the first three octets for the network ID  
1st octet starts with 1 1 0, remaining 21 bits (3 octets) complete network ID  
Last octet (8 bits) represents the host ID --> 254 hosts per network  
Class C network number values: **\[192, 223]**

- Public IP Range: 192.0.0.0 to 223.255.255.0
- Private IP Range: 192.168.0.0 to 192.168.255.255
- Subnet Mask: 255.255.255.0 (24 bits)
- Number of Networks: 2 097 150
- Number of Hosts per Network: 254
___

**Class D**: Multicasting

Not allocated to hosts, used for ***multicasting***  
Multicasting: single host sends data to multiple hosts simultaneously  
Used for streaming (e.g., ***IP-based TV***, ***stock market data***)
Class D network number values: **\[224, 239]**

- Range: 224.0.0.0 to 239.255.255.255
- Number of Networks: N/A
- Number of Hosts per Network: Multicasting (up to 268 435 456, limited by network characteristics)
___

**Class E**: Research/Experimental

Not allocated to hosts, reserved for ***research/experimental use***
Class E network number values: **\[240, 255]**

- Range: 240.0.0.0 to 255.255.255.255
- Number of Networks: N/A
- Number of Hosts per Network: Research/Reserved/Experimental
___
___

**Special IP** Addresses

- 127.0.0.1 to 127.255.255.255 
	--> network testing addresses (AKA loop-back addresses)
- "Virtual IP address": cannot be assigned to device
- 127.0.0.1 often used to troubleshoot network connectivity issues using the `ping`
	--> tests computer's TCP/IP network software driver to ensure proper working