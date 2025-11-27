https://tryhackme.com/room/raceconditionsattacks

### Table of contents
- [[#Intro]]

___
### Intro
[[#Table of contents|Back to the top]]

Race condition: situation in computer programs where **timing** of events **influences behavior** and outcome
Lack of lock mechanism and synchronization between different threads

___
### Multi-Threading
[[#Table of contents|Back to the top]]

**Program**: set of ***instructions*** to achieve task -- static

**Process** aka "job": program ***execution*** -- dynamic

**States**
![[Pasted image 20251127095228.png]]

**Thread**: lightweight ***unit of execution***, shares various memory parts and instructions with process

___
### Race Conditions
[[#Table of contents|Back to the top]]

*When one thread checks a value to perform an action, another thread might change that value before the action takes place*

Common causes
- **Parallel Execution**: handling multiple requests at the same time
- **Database Operations**: multiple users trying to read/modify/write same record at the same time --> locking mechanisms and transaction isolation
- **Third-Party Libraries and Services**: external component not designed to handle concurrent access

Test for race conditions with **Burp's Repeater**

___
### Webapp Architecture
[[#Table of contents|Back to the top]]

Client - Server

**Presentation** tier: front-end - HTML, CSS, JS
**Application** tier: webapp business logic - Node.jd, PHP, ...
**Data** tier: DBMS - MySQL

Depending on the architecture of the webapp, there can be multiple states (that check different conditions before passing to the next state) that prolong the time between the 1st verification and the final validation, making the webapp more vulnerable to race conditions


___
### Practical
[[#Table of contents|Back to the top]]

1. Study how webapp receives and responds to HTTP requests
2. Make a small transaction and intercept it
3. Send the successful transaction request to Repeater
4. Create a tab group with the request in it
5. Duplicate the request
6. Send in parallel

#### Sending group in Sequence

- **Single Connection**: establishes 1 connection --> sends all requests in group tab --> closes connection -- Test **client-side desync** vulnerability 
- **Separate Connection**: establishes 1 TCP connection --> sends 1 request --> closes connection --> repeat -- Check **Relative Start time**

#### Sending group in Parallel

Send all requests at ounce

___
### Mitigation
[[#Table of contents|Back to the top]]

- **Synchronization Mechanisms**: locks -- one thread can acquire lock at a time
- **Atomic Operations**: set of operations grouped together, executed without interruption
- **Database Transactions**: group multiple database operations into one unit --> they all succeed as a group or fail as a group