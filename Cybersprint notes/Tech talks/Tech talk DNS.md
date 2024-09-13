DNS hierarchy:
![[Pasted image 20240903133644.png]]

TLD: Top-Level Domain
SLD: Second-Level Domain (subdomain)

![[Pasted image 20240903133934.png]]

![[Pasted image 20240903134030.png]]
___

HTTP: info transmitted in plain text --> man in the middle can see everything
HTTPS: info transmitted in cipher text --> man in the middle can't understand without decryption key


DNS is not secure: info transmitted in plain text
--> man in the middle can reply DNS query and send you to malicious website -- spoofing DNS request
We could use sDNS: encrypting DNS requests
There is lobbying against sDNS because DNS provides a lot of valuable information about consumers

TOR is hiding DNS requests or using a different system