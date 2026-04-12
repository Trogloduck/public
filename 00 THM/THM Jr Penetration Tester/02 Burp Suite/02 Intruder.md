https://tryhackme.com/room/burpsuiteintruder

### Table of contents
- [[#Intro]]
- [[#Positions]]
- [[#Payloads]]
- [[#Attack Types]]
	- [[#Sniper]]
	- [[#Battering Ram]]
	- [[#Pitchfork]]
	- [[#Cluster Bomb]]
- [[#Practical 1]]
- [[#Practical 2]]
- [[#Practical 3]]

___
### Intro
[[#Table of contents|Back to the top]]

*Automated and customisable **attacks** -- modify parts of request, perform repetitive tests with variations of input data --> **fuzzing**, **brute-force***

Comparable to command-line tools like **`wfuzz`** and **`ffuf`**

Rate limitation on community edition --> use other tools for fuzzing and brute-forcing

Right-click --> Send to Intruder / **`CTRL + I

Intruder sub-tabs
- **Positions**: select attack type, configure where to insert payloads in request template
- **Payloads**: values to insert into positions defined in **Positions**; loading items from wordlist; defining pre-processing rules for each payload (e.g. adding prefix/suffix, perform match and replace, skip payloads based on defined regex)
- **Resource Pool**: not particularly useful in Community Edition, resource allocation among various automated tasks in Professional
- **Settings**: configure attack behavior, how Burp handles results and the attack itself
  Example: flag requests containing specific text, define Burp's response to redirect (3xx) responses

___
### Positions
[[#Table of contents|Back to the top]]

Burp *automatically* attempts to identify most probable position of payloads, highlighted in green and enclosed with "**`§`**"

- **`Add §`**: define new positions manually
- **`Clear §`**: removes all defined positions
- **`Auto §`**: automatically attempts to identify most likely positions based on request

___
### Payloads
[[#Table of contents|Back to the top]]

***Create**, **assign**, **configure payloads***

![[Pasted image 20251201172318.png]]
1. **Payload Sets**: choose position, select payload type
    - **Sniper and Battering Ram** only allow 1 payload set --> Payload set dropdown only has 1 option
    - **Pitchfork and Cluster Bomb** require multiple payload sets --> 1 item in dropdown for each position
    - ***Note:** when assigning numbers in "Payload Set" dropdown for multiple positions, follow **top-to-bottom, left-to-right order***
2. **Payload settings**: options specific to selected payload type for current payload set
3. **Payload Processing**: rules to be applied to each payload in set before it is sent to target
    - Example: capitalize every word, skip payloads that match regex pattern, apply other transformations or filtering
4. **Payload Encoding**: customize encoding options for payloads (default: URL encoding)

___
### Attack Types
#### Sniper
[[#Table of contents|Back to the top]]
*Cycles through payloads, inserting **one payload at a time** into each position defined in request, precise and focused testing*

**Positions:** `username=§pentester§&password=§Expl01ted§`
**Payload:** wordlist containing the words `burp`, `suit`, `intruder`

| Request Number | Request Body                           |
| -------------- | -------------------------------------- |
| 1              | `username=burp&password=Expl01ted`     |
| 2              | `username=suite&password=Expl01ted`    |
| 3              | `username=intruder&password=Expl01ted` |
| 4              | `username=pentester&password=burp`     |
| 5              | `username=pentester&password=suite`    |
| 6              | `username=pentester&password=intruder` |
Number of requests = number of words \* number of positions

#### Battering Ram
[[#Table of contents|Back to the top]]
*Sends **all payloads simultaneously**, each payload inserted into its respective position, testing for race conditions for instance*

**Positions:** `username=§pentester§&password=§Expl01ted§`
**Payload:** wordlist containing the words `burp`, `suit`, `intruder`

| Request Number | Request Body                          |
| -------------- | ------------------------------------- |
| 1              | `username=burp&password=burp`         |
| 2              | `username=suite&password=suite`       |
| 3              | `username=intruder&password=intruder` |

#### Pitchfork
[[#Table of contents|Back to the top]]
*Simultaneous testing of **multiple positions** with **different payloads**. Define multiple payload sets, each associated with specific position in request.*

**Positions:** `username=§pentester§&password=§Expl01ted§`
**Payloads:** one set per position (max 20)
- Wordlist 1 (username): `joel`, `harriet`, `alex`
- Wordlist 2 (password): `J03l`, `Emma1815`, `Sk1ll`

|Request Number|Request Body|
|---|---|
|1|`username=joel&password=J03l`|
|2|`username=harriet&password=Emma1815`|
|3|`username=alex&password=Sk1ll`|

#### Cluster Bomb
[[#Table of contents|Back to the top]]
***Sniper x Pitchfork**: Sniper-like attack on each position but **simultaneously tests all payloads from each set**. Multiple positions have different payloads, and we want to test them all together.*

**Positions:** `username=§pentester§&password=§Expl01ted§`
**Payloads:** one set per position (max 20)
- Usernames: `joel`, `harriet`, `alex`
- Passwords: `J03l`, `Emma1815`, `Sk1ll`

| Request Number | Request Body                         |
| -------------- | ------------------------------------ |
| 1              | `username=joel&password=J03l`        |
| 2              | `username=harriet&password=J03l`     |
| 3              | `username=alex&password=J03l`        |
| 4              | `username=joel&password=Emma1815`    |
| 5              | `username=harriet&password=Emma1815` |
| 6              | `username=alex&password=Emma1815`    |
| 7              | `username=joel&password=Sk1ll`       |
| 8              | `username=harriet&password=Sk1ll`    |
| 9              | `username=alex&password=Sk1ll`       |
*Tests every possibility*

___
### Practical 1
[[#Table of contents|Back to the top]]

`http://10.80.153.81/support/login`

1. Inspect Source Page of login page
```HTML
<form method="POST">
	<div class="form-floating mb-3">
		<input class="form-control" type="text" name=username placeholder="Username" required>
		<label for="username">Username</label>
	</div>
	<div class="form-floating mb-3">
		<input class="form-control" type="password" name=password placeholder="Password" required>
		<label for="password">Password</label>
	</div>
	<div class="d-grid"><button class="btn btn-primary btn-lg" type="submit">Login!</button></div>
</form>
```

2. Download leaked credentials: `wget http://10.80.153.81:9999/Credentials/BastionHostingCreds.zip`
   `unzip BastionHostingCreds.zip`
3. **Attempt** to login and **capture** login request in Proxy, **send** to Intruder
4. **Auto position** (username and password)
5. Select **Pitchfork** attack type
6. Load `usernames.txt` in position 1 and `passwords.txt` in position 2
7. **Start attack**
8. Identify successful authentication:
   - Status codes don't differentiate
   - Response length can differentiate
     --> `m.rivera:letmein1`

___
### Practical 2
[[#Table of contents|Back to the top]]

We have gained access to the support system
We identify the URL structure: `http://10.80.153.81/support/ticket/NUMBER`
--> possible [[5 IDOR|IDOR]]

1. Capture opening a ticket, send to Intruder
2. Set position to number of the ticket
3. Configure payload to a list from 1 to 100
4. Investigate the numbers returning a status code 200: `6`, `47`, `57`, `78`, `83`

___
### Practical 3
[[#Table of contents|Back to the top]]

`http://10.80.153.81/admin/login/`

1. Capture and send request to this page
   --> we see `username`, `password` AND **`loginToken`** (hidden field) need to be sent in the request
2. Refreshing the page, `session cookie` and `loginToken` change => every login attempt, we need to extract valid values for both `session cookie` and `loginToken`
   Can be done using **Burp Macros**: define set of actions (macros) to be done before each request
   In this case, it needs to extract the session cookie and loginToken in order to update them in each request

3. Capture and send login attempt
4. Pitchfork attack type
5. Set positions `username` and `password` (macros will handle other positions)
6. Load same payloads as in Practical 1

**Macros**
7. Go to Settings > Sessions > Macros > Add
	- Select the GET request to `/admin/login/` > OK > Name macro > OK
8. Still in Sessions > Session Handling Rules > Add
	- Write description > Scope > URL Scope > Use suite scope (only operate on sites added to global scope)
	- Back to Details > Add > Run a macro
		- Select macro created at step 7
		- Update only the following parameters > Add "loginToken"
		- Update only the following cookies > Add "session"
		- OK

9. **Start attack**
	--> `o.bennett:bella1`