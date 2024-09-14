AKA Internet Protocol Suite, following the [[00 OSI]] standards

| TCP/IP layer   | Working Protocol                                   |
| -------------- | -------------------------------------------------- |
| Application    | DNS, DHCP, BOOTP, SMTP, POP, IMAP, FTP, TFTP, HTTP |
| Transport      | UDP, TCP                                           |
| Internet       | IP, NAT, ICMP, OSPF, EIGRP                         |
| Network Access | ARP, PPP, Ethernet, Interface Drive                |

**Application Protocols**

- **DNS** (Domain Name System): Translates domain names into IP addresses
- **BOOTP** (Bootstrap Protocol): old DHCP; assigns IP addresses
- **DHCP** (Dynamic Host Configuration Protocol): Dynamically assigns IP addresses and reuses unused ones
- **SMTP** (Simple Mail Transfer Protocol): Sends emails from clients to servers and between servers
- **POP** (Post Office Protocol): Downloads emails from a server to a client
- **IMAP** (Internet Message Access Protocol): Accesses and stores emails on a server
- **FTP** (File Transfer Protocol): Transfers files between hosts
- **TFTP** (Trivial File Transfer Protocol): Transfers files without connection or acknowledgment
- **HTTP** (Hypertext Transfer Protocol): Transfers media, text, and graphics over the web

**Transport Protocols**

- **UDP** (User Datagram Protocol): Transfers packets without acknowledgment
- **TCP** (Transmission Control Protocol): Reliable communication with acknowledgment

**Internet Protocols**

- **IP** (Internet Protocol): Packs messages and indicates destination
- **NAT** (Network Address Translation): Converts local addresses to global ones
- **ICMP** (Internet Control Message Protocol): Signals errors during transmission
- **OSPF** (Open Shortest Path First): Routes packets using hierarchical zones
- **EIGRP** (Enhanced Interior Gateway Routing Protocol): Cisco protocol for routing with bandwidth metrics

**Network Access Protocols**

- **ARP** (Address Resolution Protocol): Maps IP addresses to physical addresses
- **PPP** (Point-to-Point Protocol): Encapsulates packets for serial connections
- **Ethernet**: Defines cabling and signaling rules for local networks
- **Interface Drivers**: Enable communication with network interfaces