**PDF**: `pdfinfo document.pdf`

**Image**: `exiftool image.jpg`

**CAPA**: Describe common behaviors: what the program is capable of doing (network communication, file manipulation, process injection, ...)

**REMnux**: Linux distribution including Volatility, YARA, Wireshark, oledump, INetSim (Internet Services Simulation Suite -- dynamic analysis), and a sandbox-like environment to dissect potentially malicious software without risking primary system
- **`oledump.py`**: static analysis of OLE2 files (Object Linking and Embedding) -- Structured Storage / Compound File Binary Format
- **`inetsim`**: simulate network activity of malware
- Volatility (**`vol3`**): analyze memory images

**[[FlareVM]]** (Forensics, Logic Analysis, and Reverse Engineering)