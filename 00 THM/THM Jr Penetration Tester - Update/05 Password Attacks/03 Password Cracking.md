https://tryhackme.com/room/passwordcracking

### Table of contents
- [[#Password Storage]]
- [[#Hash Types]]
- [[#Different Attacks]]
- [[#John the Ripper & Hashcat]]

___
### Password Storage
[[#Table of contents|Back to the top]]

4 important properties of hashing algorithms
- **One-way**
- **Deterministic**
- **Fixed-length output**
- **Collision-resistant:** 2 different inputs can't produce same hash --> when it happens algo is deprecated (MD5 and SHA-1)

| Algorithm | Output Length             | Still Used for Passwords?           | Notes                                      |
| --------- | ------------------------- | ----------------------------------- | ------------------------------------------ |
| MD5       | 128 bits (32 hex chars)   | No                                  | Fast, collision-prone, widely cracked      |
| SHA-1     | 160 bits (40 hex chars)   | No                                  | Faster than SHA-256, deprecated            |
| SHA-256   | 256 bits (64 hex chars)   | Sometimes                           | Better than MD5/SHA-1 but still fast       |
| NTLM      | 128 bits (32 hex chars)   | Yes (legacy Windows authentication) | MD4-based, used for Windows account hashes |
| bcrypt    | ~ 60 chars, `$2*$` prefix | Yes, recommended                    | Deliberately slow, cost-configurable       |
| Argon2    | Variable                  | Yes, recommended                    | Modern standard, memory-hard               |
MD5, SHA-1, SHA-256 designed for file integrity checks and digital signatures, not password storage

##### Salting

Solves 2 problems
- **Collision** due to 2 users having same password
- Attacker able to use **rainbow table**

Salt: unique random string generated for each user
```
stored_value = hash(password + salt)
```

Salt is stored alongside hash in database

___
### Hash Types
[[#Table of contents|Back to the top]]

| Hash Type | Length       | Prefix / Format           | Example                                                          |
| --------- | ------------ | ------------------------- | ---------------------------------------------------------------- |
| MD5       | 32 hex chars | None                      | 5f4dcc3b5aa765d61d8327deb882cf99                                 |
| SHA-1     | 40 hex chars | None                      | 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8                         |
| SHA-256   | 64 hex chars | None                      | 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 |
| NTLM      | 32 hex chars | None                      | 8846f7eaee8fb117ad06bdd830b7586c                                 |
| bcrypt    | ~60 chars    | `$2a$`, `$2b$`, or `$2y$` | `$2y$12$`...                                                     |

**MD5 vs NTLM:** only context can tell, in doubt test both
e.g. : hash extracted from Windows SAM / Active Directory --> very likely NTLM
	vs from webapp database --> MD5, or SHA variant

**bcrypt:** "12" in above example is "cost factor", controls how slow hash computation is

##### Automated Tools

**`hashid`**

`apt install hashid`

`hashid '5f4dcc3b5aa765d61d8327deb882cf99'`

**`hashcat`**

`hashcat --identify '5f4dcc3b5aa765d61d8327deb882cf99'`

Once algo identified, feed it to hashcat / John the Ripper with right mode/format

| Algorithm | `-m` | `--format=` |
| --------- | ---- | ----------- |
| MD5       | 0    | raw-md5     |
| SHA-1     | 100  | raw-sha1    |
| SHA-256   | 1400 | raw-sha256  |
| SHA-512   | 1700 | raw-sha512  |
| NTLM      | 1000 | nt          |
| bcrypt    | 3200 | bcrypt      |

**Online tools:** crackstation.net, hashes.com
>**/!\ Never use on corporate engagement:** hash could contain sensitive info

___
### Different Attacks
[[#Table of contents|Back to the top]]

##### Dictionary
Fast starting point, `rockyou.txt` is really good, SecLists for broader coverage

##### Brute-Force
Rarely viable beyond 6-7 characters, makes sense for 4-digit PIN / very constrained pattern

##### Rule-Based
Take existing wordlist, apply transformation that people commonly use having to follow password policies
- Capitalise 1st letter
- Append number
- Add special character
- Substitute character (`p@ssword`)
*Extends coverage without going full brute-force*

Rule files
- `best64.rule`: 64 highly effective mutations, good 1st choice
- `rockyou-30000.rule`: 30 000 rules from RockYou analysis
- `d3ad0ne.rule`: large community-built rule set
- `dive.rule`: extensive rule set covering wide range of mutations
- `OneRuleToRuleThemAll.rule`: popular community-compiled rule set, not bundled by default

##### Mask
Structured brute-force attack --> regex
Hashcat mask syntax
- `?l`: lowercase letter
- `?u`: uppercase letter
- `?d`: digit
- `?s`: special characater
- `?a`: any printable ASCII

##### Choose Right Approach
- **No info:** dictionary with `rockyou.txt`
- Dictionary failed, password likely **mutated:** dictionary + rules
- Known password **pattern** / enforced **policy:** mask
- **Short** password / **small** character set: brute-force
- Target likely used **company-specific** terms: custom wordlist + rules

___
### John the Ripper & Hashcat
[[#Table of contents|Back to the top]]

[[John the Ripper]]

##### John the Ripper
Dictionary
```Shell
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt demo.txt
```
Rule-based
```Shell
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt --rules=wordlist demo2.txt
```
View Cracked Passwords
```Shell
john --show --format=raw-md5 demo.txt
```

##### Hashcat
Dictionary (`-a 0`: attack mode = 0)
```Shell
hashcat -m 0 -a 0 demo.txt /usr/share/wordlists/rockyou.txt
```
Rule-based
```Shell
hashcat -m 0 -a 0 demo2.txt /usr/share/wordlists/rockyou.txt -r /usr/local/hashcat/rules/best64.rule
```
Mask
```Shell
hashcat -m 0 -a 3 demo3.txt '?l?l?l?l?l?l?l?l'
```
Save output to file: `-o cracked.txt`
View output after cracked
```Shell
hashcat -m 0 demo.txt --show
```

Long Hashcat runs --> use `--session=name_of_session`, then `--session=name_of_session --restore` if interrupted

Comparison
- John: quick attempts, varied formats, shadow files
- Hashcat: sustained attacks, GPU-accelerated cracking