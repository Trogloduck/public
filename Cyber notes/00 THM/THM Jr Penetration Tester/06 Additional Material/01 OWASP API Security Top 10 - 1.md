https://tryhackme.com/room/owaspapisecuritytop105w

### Table of contents
- [[#API]]
- [[#1. BOLA - Broken Object Level Authorization]]
- [[#2. BUA - Broken User Authentification]]
- [[#3. Excessive Data Exposure]]
- [[#4. Lack of Resources & Rate Limiting]]
- [[#5. Broken Function Level Authorization]]

___
### API
[[#Table of contents|Back to the top]]

Application Programming Interface: middleware, facilitating communication between 2 softwares via requests and responses

___
### 1. BOLA - Broken Object Level Authorization
[[#Table of contents|Back to the top]]

API endpoints retrieve and manipulate data through object identifiers, BOLA is a kind of [[5 IDOR|IDOR]] --> user uses input to access resources they shouldn't have access to

*Example*

**Context:** 
API with endpoint `/apirule1/users/{ID}`
Applications/developpers can request info by sending ID

**Problem:** no validation of requests as valid, no checking for authorization
**Solution:** ***access tokens / authorization*** tokens in request headers

___
### 2. BUA - Broken User Authentification
[[#Table of contents|Back to the top]]



___
### 3. Excessive Data Exposure
[[#Table of contents|Back to the top]]



___
### 4. Lack of Resources & Rate Limiting
[[#Table of contents|Back to the top]]



___
### 5. Broken Function Level Authorization
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
