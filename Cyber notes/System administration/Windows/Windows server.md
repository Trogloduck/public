1. Configure server to perform routing for clients connected to it in LAN

**On the client**, Windows + R, `ncpa.cpl` > Live Migration > Properties > Internet Protocol Version 4 > Default gateway: the IP of the interface for internet on the server (Ethernet) ; DNS: the IP of the server

**On the server**, Add roles and features > tick `Remote Access` > Role services > tick `Routing`

Windows + R, `wf.msc` > Inbound rules > New rule > Custom > Protocol: ICMPv4 >> Name: Allow ICMPv4

Tools > Routing and Remote access > DC (local) > click/right-click > Configure and Enable Routing and Remote Access > Custom configuration > LAN/NAT (?) routing >> Start service