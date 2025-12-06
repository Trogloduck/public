https://tryhackme.com/room/oscommandinjection

### Table of contents
- [[#Command Injection]]
- [[#Remediation]]

___
### Command Injection
[[#Table of contents|Back to the top]]

Using privilege of application to execute commands on device application is running on

Detect command injection
1. **Blind** command injection: no direct output from webapp, investigate app behavior
--> Use payload that causes **time delay**: **`ping`** (app hangs for x seconds depending on number of pings sent), **`sleep`**
--> **Force** an **output** using redirection (**`>`**): `whoami > forced_output.txt; cat forced_output.txt`
*Example*: `curl http://vulnerable.app/process.php%3Fsearch%3DThe%20Beatles%3B%20whoami`
URL decoded: `?search=The Beatles; whoami`

2. **Verbose** command injection: direct feedback from webapp (running `whoami`for instance)
Payloads: `whoami`, `ls`/`dir`, `ping`, `sleep`/`timeout`, `nc`(reverse shell)


___
### Remediation
[[#Table of contents|Back to the top]]

PHP: functions that can interact with OS to execute commands
- `exec`
- `passthru`
- `system`

Use a `pattern`in order to allow only certain characters as input (only numbers for instance)

**Sanitization**: only numerical data / remove `>`, `&`, `/`
`filter_input(input, "name_of_variable_to_filter", filter to apply)`

**Bypassing Filters**
`$payload = "\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64"`
(from Hex, delimiter `\x`: `/etc/passwd`)