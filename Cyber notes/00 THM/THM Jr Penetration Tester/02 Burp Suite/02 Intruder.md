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
- 

___
### Intro
[[#Table of contents|Back to the top]]

Automated and customisable attacks -- modify parts of request, perform repetitive tests with variations of input data --> fuzzing, brute-force

Comparable to command-line tools like wfuzz and ffuf

Rate limitation on community edition --> use other tools for fuzzing and brute-forcing

Right-click on request and Send to Intruder / **`CTRL + I

Intruder sub-tabs
- **Positions**: select attack type, configure where to insert payloads in request template
- **Payloads**: values to insert into positions defined in **Positions**; loading items from wordlist; defining pre-processing rules for each payload (e.g. adding prefix/suffix, perform match and replace, skip payloads based on defined regex)
- **Resource Pool**: not particularly useful in Community Edition, resource allocation among various automated tasks in Professional
- **Settings**: configure attack behavior, how Burp handles results and the attack itself
  Example: flag requests containing specific text, define Burp's response to redirect (3xx) responses

___
### Positions
[[#Table of contents|Back to the top]]

Burp *automatically* attempts to identify most probable position of payloads, highlighted in green and enclosed with "`§`"

- `Add §`: define new positions manually
- `Clear §`: removes all defined positions
- `Auto §`: automatically attempts to identify most likely positions based on request

___
### Payloads
[[#Table of contents|Back to the top]]

*Create, assign, configure payloads*

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
*Cycles through payloads, inserting one payload at a time into each position defined in request, precise and focused testing*

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
*Sends all payloads simultaneously, each payload inserted into its respective position, testing for race conditions for instance*



#### Pitchfork
[[#Table of contents|Back to the top]]
*Simultaneous testing of multiple positions with different payloads. Define multiple payload sets, each associated with specific position in request.*



#### Cluster Bomb
[[#Table of contents|Back to the top]]
*Sniper x Pitchfork: Sniper-like attack on each position but simultaneously tests all payloads from each set. Multiple positions have different payloads, and we want to test them all together.*



___
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
