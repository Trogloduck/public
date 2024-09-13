< [[00 Networking]]

Address Resolution Protocol enables device to match MAC with IP in a network, devices will store other devices MAC-IP in their ARP table (ARP entry), reverse ARP is matching an IP with a MAC, works on the local lvl

- ARP request: device asks for specific MAC, sent to every device on the network
	- ARP reply: device with specific MAC answers

 --> Man in the middle: ARP poisoning

Ex: Wi-Fi box uses ARP to assign IP to my computer