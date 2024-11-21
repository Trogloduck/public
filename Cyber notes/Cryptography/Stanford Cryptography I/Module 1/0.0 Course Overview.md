# Cryptography is everywhere

- Communication
	- Web traffic: HTTPS
	- Wireless traffic: 802.11i WPA2, GSM, Bluetooth
- Disk files
	- EFS, TrueCrypt
- Physical content
	- DVD --> CSS; Blu-ray --> AACS
- Authentication
- ...

# SSL-TLS

Secure Sockets Layer - Transport Layer Security

Protocol used to secure communication between 2 devices, prevent eavesdropping and tampering

2 main parts:
1. Handshake protocol: establish shared secret key
2. Record layer: transmit data using shared secret key

# Building block

Symmetric encryption systems

1 secret key, shared by all users

2 algorithms, E & D (encryption and decryption)

m, c (message, cipher)

![[sym_encrypt.png.png#center]]

**/!\\** *Always use encryption algorithms that are public: they have been peer reviewed*

### Use cases
- Single use key (one time key): used to encrypt 1 message (new key generated for each email)
- Multi use key (many time key): encrypting files --> same key for multiple files