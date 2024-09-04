Routers are just computers composed of an IOS (Internetwork Operating System), a processor, RAM and ROM

Configuration:

- Enter the interface configuration mode
	`interface gigabitethernet 0/0`
- We configure the network of the interface
	`ip address 192.168.10.1 255.255.255.0`
- Configure the default gateway
	`ip default-gateway 192.168.10.50`
- Give a description for the interface
	`description Link to LAN-10`
- (Re)start the interface
	`no shutdown`

Check configuration: 

- `show ip interface brief`: overview of interfaces
- `show ip route`: routing table
- `show interfaces`: interface statistics
- `show ip interface`: IPv4 statistics for interfaces

