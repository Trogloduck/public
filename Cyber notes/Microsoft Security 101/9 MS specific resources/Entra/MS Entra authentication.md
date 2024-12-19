![[Pasted image 20241217141219.png]]

- **Password**
- **Phone**: SMS-based (can be used as primary authentication method), Voice call verification (cannot be used as primary method)
- **OATH** (Open Authentication): TOTP (Time-based One-Time Password)
	- **Software**: app generates secret key /seed used to generate OTP
	- **Hardware**: small hardware device like a key fob, displays code every 30-60 seconds, secret key /seed associated with hardware input into Entra to use this as an authentication method
- **Passwordless**
	- **Windows Hello** for Business: 2FA, PIN or biometric trigger private key to cryptographically sign data sent to identity provider
	- **FIDO2** (Fast Identity Online): open standard for passwordless, security key built into typically USB device (/bluetooth, NFC)
	- **MS Authenticator app**
		- Converts iOS/Android phone into strong passwordless credential, match number and use biometric/PIN to confirm
		- Can generate OATH
	- **CBA** (Certificate-Based Authentication): X.509 certificate, part of PKI (Public Key Infrastructure), digitally signed document binding identity to public key

![[Pasted image 20241217144117.png]]
