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

**Context** 
API with endpoint `/apirule1/users/{ID}`
Applications/developpers can request info by sending ID

**Problem:** no validation of requests as valid, no checking for authorization

**Solution:** ***access tokens / authorization*** tokens in request headers

___
### 2. BUA - Broken User Authentification
[[#Table of contents|Back to the top]]

Invalid implementation of authentication (e.g. incorrect email/password queries, ...) / absence of security mechanisms (e.g. authorization headers, tokens, ...)

*Example*

**Context** 
- API endpoint for authentication: `apirule2/user/login_v`
- Endpoint returns token, passed as `Authorization-Token` header (GET) to `apirule2/user/details` 
- Email is used to validate user from `user-table`, ignored password field in SQL query

**Problem:** attacker only requires victim's email to get valid token, which they can then send with a GET request to `login_v` endpoint

**Solutions**
- Require email and password for authentication
- **Complex** passwords
- **No GET/POST** requests to send credentials
- **JWT** (JSON Web Token), authorization **headers**, ...
- **Multifactor** authentication, account **lockout**, **captcha**
- **Hash** passwords

___
### 3. Excessive Data Exposure
[[#Table of contents|Back to the top]]

Application developers left filtering task to front-end developers --> attacker can intercept response through API by sniffing traffic

*Example* 

**Context**
Comment-based web portal, stores comments in database (+ location, device info, ...)
Endpoint `apirule3/comment_v/{id}`

**Problem**: too much data is sent (not just the relevant one)

**Solutions**
- Don't leave sensitive data filtration to front-end dev
- Time-to-time review of response from API 
- Avoid generic methods such as `to_string()` and `to_json()`
- Test various cases for data leaks

___
### 4. Lack of Resources & Rate Limiting
[[#Table of contents|Back to the top]]

No restriction on frequency of clients requests, files size, ...
--> DoS, unavailability

*Example*

**Context**
Email marketing plan --> send marketing, password recovery emails, ...
--> "Forgot Password" option required
Endpoint `/apirule4/sendOTP_v` sends 4-digit numeric code to user's email

**Problem:** no rate limiting on number of requests possible --> possible to overload endpoint in order to brute-force it and send emails on behalf of the company

**Solution**
- **Captcha**
- **Limit**, alert when exceeded
- **Maximum** data **size** on all parameters

___
### 5. Broken Function Level Authorization
[[#Table of contents|Back to the top]]

Low privileged user bypasses system checks, gets access to confidential data by impersonating high privileged user
APIs with complex user roles and permissions that can span hierarchy more prone to this

*Example* 

**Context**
- Develop admin dashboard, view employee data and perform tasks
- Endpoint `/apirule5/users_v` fetch employees data from database
- Special header `isAdmin` in each request, API only fetches if this header = 1 and `Authorization-Token` is correct

**Problem:** non-admin user that has correct `Authorization-Token` can access employee data by setting `isAdmin` to 1

**Solutions**
- Proper design, testing all authorization systems, deny by default
- Operations allowed only to users belonging to authorized group(s)
- Review API endpoints