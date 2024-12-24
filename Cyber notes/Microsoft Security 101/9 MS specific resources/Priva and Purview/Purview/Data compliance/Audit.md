Logging system, helps with (compliance) investigations and forensics, integrates Copilot

#### Standard

Audited activity performed > audit record generated and stored in audit log for $\leq$ 180 days

Retrieved audit logs
- Audit log search tool in MS Purview portal
- 365 Management Activity API
- Search-UnifiedAuditLog cmdlet in Exchange Online PowerShell

Can export logs in .csv file for further investigation

#### Premium

- Log retention policies $\leq$ 1 years ($\leq$ 10 years for users with required add-on license)
- Entra ID, Exchange, OneDrive, SharePoint $\leq$ 1 year, other 180 days by default
- Intelligent insights
- Higher bandwidth to 365 Management Activity API