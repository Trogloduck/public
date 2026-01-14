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

Invalid implementation of authentication (e.g. incorrect email/password queries, ...) / absence of security mechanisms (e.g. authorization headers, tokens, ...)

Example

**Context:** 
API endpoint for authentication: `apirule2/user/login_v` 
Endpoint returns token, passed as `Authorization-Token` header (GET) to `apirule2/user/details` 
Email is used to validate user from `user-table`, ignored password field in SQL query

**Problem:** attacker only requires victim's email to get valid token, which they can then send with a GET request to `login_v` endpoint

**Solutions:**
- Require email and password for authentication
- **Complex** passwords
- **No GET/POST** requests to send credentials
- **JWT** (JSON Web Token), authorization **headers**, ...
- **Multifactor** authentication, account **lockout**, **captcha**
- **Hash** passwords

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
