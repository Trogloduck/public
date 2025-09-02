*hash cracking tool*
### Table of contents
- [[#Installation]]
- [[#Basic Hashes]]
- [[#Windows authentication hashes]]
- [[#`/etc/shadow` hashes]]
- [[#Single Crack Mode]]
- [[#Custom Rules]]
- [[#Password-protected Zip files]]
- [[#Password-protected RAR files]]
- [[#SSH keys]]
___
### Installation
[[#Table of contents|Back to the top]]

Kali has Jumbo John installed

`john`: check version of Jumbo John

[Installation guide](https://github.com/openwall/john/blob/bleeding-jumbo/doc/INSTALL)

Downloadable for Windows [here](https://www.openwall.com/john/)

Need a wordlist for dictionary attack $\rightarrow$ [SecLists](https://github.com/danielmiessler/SecLists)

Kali has great wordlists @ /usr/share/wordlists

### Basic Hashes
[[#Table of contents|Back to the top]]

Basic syntax: `john [options] [file path]`

If hash type unknown, **automatic** option:
`john --wordlist=[path to wordlist] [path to file]`

*Example*:
`john --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt`

Or **identify hash type**
https://hashes.com/en/tools/hash_identifier
https://gitlab.com/kalilinux/packages/hash-identifier/-/tree/kali/master

Hash type known $\Rightarrow$ **format-specific** cracking
`john --format=[format] --wordlist=[path to wordlist] [path to file]`

When providing the **raw hash** (no username, salt, no encoding or formatting), some format require the "raw" specification

*Example*:
`john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt`

`john --list=formats`: determine if "raw" is required, combine it with `| grep -iF "[format]"`

### Windows authentication hashes
[[#Table of contents|Back to the top]]
### `/etc/shadow` hashes
[[#Table of contents|Back to the top]]
### Single Crack Mode
[[#Table of contents|Back to the top]]
### Custom Rules
[[#Table of contents|Back to the top]]
### Password-protected Zip files
[[#Table of contents|Back to the top]]
### Password-protected RAR files
[[#Table of contents|Back to the top]]
### SSH keys
[[#Table of contents|Back to the top]]
