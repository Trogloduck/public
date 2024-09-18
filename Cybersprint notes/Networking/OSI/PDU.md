<[[00 OSI]]

**Protocol Data Unit**: general term used to describe block of data exchanged between layers of OSI model. Each layer of the OSI model has its own PDU:

- **Application Layer:** *Data*
- **Presentation Layer:** *Data*
- **Session Layer:** *Data*
- **Transport Layer:** segments/reassembles data into/from *smaller chunks* (***segment*** for TCP or ***datagram*** for UDP)
- **Network Layer:** *encapsulates* segment/datagram into a ***packet*** (raw data, routing and addressing information)
- **Data Link Layer:** encapsulates packet into ***[[Frame]]*** for local network transmission
- **Physical Layer:** *Bit* (though not typically called PDU, it represents raw data transmitted over physical medium)