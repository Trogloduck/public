< [[4. Transport]]

Transmission Control Protocol: ***checks*** if you actually received data and resends it if you didn’t, ensures more ***integrity*** of data thanks to ***error checking***
--> file sharing, internet browsing, email sending/receiving

**TCP header fields**
- **Source Port** (16 bits)
- **Destination Port** (16 bits)
- **Sequence Number** (32 bits): keeps track of order of bytes sent
- **Acknowledgment Number** (32 bits): receipt
- **Data Offset (Header Length)** (4 bits)
- **Reserved** (3 bits): reserved for future use, must be set to zero
- **Flags (Control bits)** (9 bits): control flags (URG, ACK, PSH, RST, SYN, FIN) manage connection states and data flow
- **Window Size** (16 bits): size of sender's receive window (buffer space)
- **Checksum** (16 bits): error-checking for header and data
- **Urgent Pointer** (16 bits): points to urgent data if URG flag is set
- **Options** (variable): additional functionalities, such as maximum segment size
- **Padding** (variable): ensures TCP header is a multiple of 32 bits in length
___

**TCP connection**
1. **Check Destination Device**: present and reachable on network
2. **Verify Application**: destination device has application listening on specified port
3. **Send Connection Request**: inform destination device of connection request via handshake process

**Handshake**: confirms identity of connecting systems and enables communication

SYN
1. **Synchronization** (SYN) packet (host A --> server B): initial request to start connection. SYN packet includes randomly generated sequence number.
2. **SYN Reception** (by server B): server acknowledges it has received request and is ready to respond

SYN-ACK
3. **Synchronization-Acknowledgment (SYN-ACK)** packet (server B --> host A):
    - acknowledges receipt of SYN packet (ACK)
    - includes its own SYN packet with a randomly generated sequence number
4. **SYN-ACK Reception** (by host A): client receives server's response and is ready to proceed

ACK
5. **Acknowledgment (ACK)** packet (host A --> server B): client confirms receipt of SYN-ACK and includes next expected sequence number
6. **ACK Reception** (by server B): server confirms receipt of client's ACK; connection is established

Possible *outcomes* of handshake:
- **No Response** (unavailable or protocol not supported)
- **Connection Rejected**
- **Connection Accepted**

For connection termination, the handshake process is the same but with FIN instead of SYN (SYN and FIN are control flags)

**Control flags**: included in TCP header, modifies behavior of TCP request
- ***URG*** (urgent): priority data packet
- ***PSH*** (push): data pushed to application without being buffered
- ***RST*** (reset): reset connection