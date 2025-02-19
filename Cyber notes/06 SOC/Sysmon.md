https://github.com/microsoft/SysmonForLinux

### Installation

**Kali installation** (Debian 12)

Register Microsoft key and feed:
```bash
wget -q https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
```

Installation:
```bash
sudo apt-get update
sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install sysmonforlinux
```

### Configuration

