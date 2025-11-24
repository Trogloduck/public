### Table of contents
- [[#Types of Firewalls]]

___
### Types of Firewalls
[[#Table of contents|Back to the top]]

##### Stateless
- OSI Layers 3 and 4
- Filters data based on predetermined rules, regardless of state of previous connections
- High-speed

##### Stateful
- OSI Layers 3 and 4
- Keeps track of previous connections
- Recognize traffic patterns, monitor connections

##### Proxy -- Application-level Gateway
- Intermediate between private network and internet on layer 7 --> Application control
- Inspect content of packets --> Content filtering policies available
- SSL/TLS decryption

##### Next-Generation
- OSI Layers 3 to 7
- Deep packet inspection
- IDS
- Heuristic analysis, analyzes patterns
- SSL/TLS decryption
- Correlate with threat intelligence feeds


___
### Rules
[[#Table of contents|Back to the top]]

- **Source address**
- **Destination address**
- **Port**
- **Protocol**
- **Action** (to be taken if such traffic is identified)
- **Direction**

Actions: Allow, Deny, Forward (redirect to Destination address)


___
### Linux
[[#Table of contents|Back to the top]]

Netfilter
- **`iptables`**
- **`nftables`**: successor of `iptables`
- **`firewalld`**

**`ufw`** (uncomplicated firewall)