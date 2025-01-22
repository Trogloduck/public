< [[4. Transport]]

User Datagram Protocol: ***faster*** and more adequate for ***real-time*** data sharing
--> multiplayer FPS game for instance, while when you open a shop it would use TCP; videocall

**UDP header fields**
- **Source port** (16 bits)
- **Destination port** (16 bits)
- **Length** (16 bits): header + data
- **Checksum** (16 bits): error-checking for header and data

Unlike TCP, no handshake is required, no connection setup, relies on connection established at physical and data-link layers