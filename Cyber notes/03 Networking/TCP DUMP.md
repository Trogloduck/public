`man tcpdump`

Every command will start with `tcpdump` and then will use different options to modify the request

`-i [INTERFACE]`: specify which network interface to listen to
	$\Rightarrow$ `-i any`, `-i eth0`
	
> `ip address show` or `ip a s`: display available network interfaces

`-w [FILE]`: save network traffic for in a .pcap file for later inspection

`-r [FILE]`: read packets from file

`-c [COUNT]`: limit number of packets to be captured / interrupt with CTRL+C

TCPDUMP automatically resolves IP addresses (DNS lookup) and ports (80 replaced with http for instance)
	$\rightarrow$ `-n` prevents DNS lookup, `-nn` prevents both DNS and port resolution

`-v`: verbose mode (more details), `-vv`, `-vvv` even more

`host [IP]/[HOSTNAME]`: filter by **host** IP/name
	`src/dst host [IP/HOSTNAME]`: limit packets to particular **source or destination IP**/name

`port [PORTNUMBER]`: filter by **port**, for instance `port 53` will only return DNS traffic
	`src/dst port [PORTNUMBER]`

Can limit by **protocol** by simply naming the protocol (ip, icmp, ip6, udp, tcp, ...)

**Logical operators**: `and`, `or`, `not`

`greater/less [LENGTH]`: filter packets by length

`man pcap-filter`

**Binary operations**:
Applied on bits (0/1)
- `&`: "and", 0 unless both bits are 1
- `|`: "or", 1, unless both bits are 0
- `!`: "not", inverts bit

`proto[expr:size]`: inspect a number of bytes in the **header** of a specified protocol
- proto: arp, ether, icmp, ip, ...
- expr: byte offset (0 = 1st)
- size: number of bytes of interest

This command is often used in conjunction with binary operations:
`ether[0] & 1 != 0`: *1st byte in Ethernet header AND 1 (0000 0001) must be different from 0 (0000 0000)*

`tcp[tcpflags]`
- tcp-syn: synchronize
- tcp-ack: acknowledge
- tcp-fin: finish
- tcp-rst: reset
- tcp-push: push

Examples:
`tcpdump "tcp[tcpflags] == tcp-syn"`: TCP packets with **only** SYN flag set
`tcpdump "tcp[tcpflags] & tcp-syn != 0"`: **at least** SYN flag set

Other **display options**:
- `-q`: quick (brief) output
- `-e`: print link-level header $\Rightarrow$ MAC addresses
- `-A`: show packet data in ASCII
- `-xx`: show packet data in hexadecimal format, referred to as hex
- `-X`: show packet headers and data in hex and ASCII