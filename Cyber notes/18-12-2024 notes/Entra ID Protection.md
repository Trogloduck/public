Identity-based risks can be fed into tools like Conditional Access or to a SIEM

Cf. sign-in/user risk in [[Entra Conditional Access]]

#### Investigation

- **Risk detections**: each risk reported as risk detection (leaked credentials, sign-ins from unfamiliar locations, malware infections, ...)
- **Risky sign-ins**: risky sign-in reported when one or more risk detections reported for that sign-in
- **Risky users**: risky user reported when
    -  user has $\geq$ 1 risky sign-in(s) and/or
    - $\geq$ 1 risk detections reported associated with account
#### Remediation

Can be automated. For instance, access control can be automated (asking for additional authentication)

#### Exportation

Used for archival, correlation with other tools (SIEM)