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

Downloads for Windows and Wiki [here](https://www.openwall.com/john/)

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
https://gitlab.com/kalilinux/packages/hash-identifier/-/tree/kali/master $\Rightarrow$ `python3 hash-id.py`

Hash type known $\Rightarrow$ **format-specific** cracking
`john --format=[format] --wordlist=[path to wordlist] [path to file]`

When providing the **raw hash** (no username, salt, no encoding or formatting), some format require the "raw" specification

*Example*:
`john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt`

`john --list=formats`: determine if "raw" is required, combine it with `| grep -iF "[format]"`

### Windows authentication hashes
[[#Table of contents|Back to the top]]

Authentication hashes: hashed versions of passwords, stored by OS
#### NTHash -- NTLM
(LM was the previous version)

NT: New Technology

SAM (Security Account Manager): store usernames and hashed passwords in Windows
Acquire hashes by dumping SAM database with Mimikatz or Active Directory database (NTDS.dit)

Sometimes no cracking is required: "**pass the hash**" attack

Cracking is great when the password policy is weak

`john --format=nt nthash.txt`

### `/etc/shadow` hashes
[[#Table of contents|Back to the top]]

Where password hashes are stored on Linux, date of last password change, expiration date, need root privileges
#### 1. Unshadowing
`/etc/shadow` must be combined with `/etc/passwd` for John to understand it
	$\rightarrow$ `unshadow [path to passwd] [path to shadow] > unshadowed.txt`

Unshadow entire files or specific line
#### 2. Crack
`john --format=sha512crypt unshadowed.txt`

### Single Crack Mode
[[#Table of contents|Back to the top]]

John tries to crack the password using heuristics based on the username

`--single`
#### Word mangling
"Markus"
- Markus1, Markus2, Markus3, ...
- MArkus, MARkus, MARKus, ...
- Markus!, Markus$, Markus*, ...
#### GECOS
*General Electric Comprehensive Operating System*
Entries in the /etc/passwd and /etc/shadow files are separated by ":"
**GECOS field**: **5**th entry, stores general info about user (full name, office number, phone number, ...)
John can take into account these for single crack method

To use single crack mode, hash must be modified:
\[raw hash] $\rightarrow$ \[username]:\[raw hash]

### Custom Rules
[[#Table of contents|Back to the top]]

When "password must contain uppercase letter, lowercase letter, number, symbol", user often build passwords like this: `Password123!`
	$\rightarrow$ uppercase precedes lowercase, then number, then symbol
	$\Rightarrow$ pattern can be exploited by attackers, using custom rules

Custom rules usually located in `/etc/john/john.conf`

Syntax: `[List.Rules:THMRules]`: define rule name
Then uses **regex style pattern** match to define where the word will be modified
- **`Az`**: **appends** with defined characters
- **`A0`**: **prepends**
- **`c`**: **capitalizes** positionally

Define characters to be appended/prepended, inside **" "**: `[characters]` $\rightarrow$ `[A-z]`, `[0-9]`, `[!£$%@]`, ...

`Password123!`
$\rightarrow$ `[List.Rules:DumbPassword]`
	**`cAz"[0-9] [!£$%@]"`**

`--rule=DumbPassword`: apply custom rule

### Password-protected Zip files
[[#Table of contents|Back to the top]]
#### 1. Zip2John
`zip2john [options] [zip file] > output.txt` (option aren't often required)
#### 2. Crack
1. `john output.txt` $\rightarrow$ password
2. `unzip file.zip` $\rightarrow$ use cracked password

### Password-protected RAR files
[[#Table of contents|Back to the top]]
#### 1. Rar2John
`rar2john [rar file] > output.txt`
#### 2. Crack
1. `john output.txt` $\rightarrow$ password
2. `unrar x -p[password] file.rar`

### SSH keys
[[#Table of contents|Back to the top]]

By default, you authenticate SSH log in using a password.
But you can use your **private key `id_rsa`** to authenticate. Doing so often requires a password to access the private key $\rightarrow$ this password can be cracked
#### 1. SSH2John
`python3 ssh2john id_rsa > output.txt`
#### 2. Crack
`john output.txt`

NB: if `john output.txt` doesn't work, try `john --wordlist=[wordlist location] output.txt`