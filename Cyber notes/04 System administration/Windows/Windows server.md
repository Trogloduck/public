1. Configure server to perform routing for clients connected to it in LAN

**On the client**, Windows + R, `ncpa.cpl` > Live Migration > Properties > Internet Protocol Version 4 > Default gateway: the IP of the interface for internet on the server (Ethernet) ; DNS: the IP of the server

**On the server**, Add roles and features > tick `Remote Access` > Role services > tick `Routing`

Windows + R, `wf.msc` > Inbound rules > New rule > Custom > Protocol: ICMPv4 >> Name: Allow ICMPv4

<<<<<<< HEAD
Tools > Routing and Remote access > DC (local) > click/right-click > Configure and Enable Routing and Remote Access > Custom configuration > LAN/NAT (?) routing >> Start service
=======
Tools > Routing and Remote access > \[name of the server] > right-click > Configure and Enable Routing and Remote Access > Custom configuration > LAN routing >> Start service
>>>>>>> 59b4e5691e17329f0abd8dbc06fc1b25d044e2f1
