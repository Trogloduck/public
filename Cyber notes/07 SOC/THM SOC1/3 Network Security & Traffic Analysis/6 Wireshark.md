*Network packet analyzer*

### Table of contents
- [[#Packet Dissection]]
- [[#Filtering]]

___
### Packet Dissection
[[#Table of contents|Back to the top]]

Refers to some of the OSI layers
1. **Frame**: *Physical* -- Ethernet / WiFi / ...
2. **Source \[MAC]**: *Data Link*
3. **Source \[IP]**: Network
4. **Protocol**: *Transport* -- UDP/TCP, ports
   **Protocol Errors**: TCP segments needing reassembling
5. **Application Protocol**: *Application* -- HTTP/FTP/SMB
   **Application Data**: application-specific data

___
### Filtering
[[#Table of contents|Back to the top]]

2 types of filter:
- **Capture**: *captures* only valid packets for used filters
- **Display**: *displays* only valid packets for used filters

##### Apply as filter
**Right-click** on field of interest > Apply as filter -- *generates query that will filter packets that have the same value for that field*
##### Prepare as Filter
Similar to Apply, prepares query but doesn't apply it immediately (> add **".. and/or.."** from right-click menu) > hit Enter to apply filter
##### Conversation filter
**Right-click** on field of interest > Conversation Filter
*Filter all linked packets (IP addresses, ports), not just based on single entity*
##### Colourise Conversation
Similar to Conversation filter but just highlights without hiding other packets
**View** > Colourise Conversation (> Reset Colourisation)
##### Apply as Column
**Right-click** on value from a packet's details > Apply as Column
##### Follow Stream
Reconstruct application level data to understand event of interest. View unencrypted data (usernames, passwords, ...)
**Right-click** > Follow TCP/UDP/HTTP Stream
Originating from server: blue
Originating from client: red