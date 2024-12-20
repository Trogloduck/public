Integrated in XDR, accessed through [[Defender portal]], under Cloud apps node

Protection for SaaS apps
- **CASB** (Cloud Access Security Broker): gatekeeper to broker real-time access between users and cloud resources, discovery into cloud app usage and shadow IT, protection against app-based threats, information protection, compliance
- **[[#SSPM]]**: SaaS Security Posture Management
- **[[#Advanced threat protection]]**: correlation of signal and visibility across full kill chain of advanced attacks
- **[[#App-to-app protection]]**: extend core threat scenarios to OAuth-enabled apps that have permissions and privileges to critical data and resources
#### Discover SaaS apps

- **Identify**: data based on assessment of network traffic and extensive app catalog to identify apps accessed by users
- **Assess**: evaluate discovered apps for 90+ risk indicators
- **Manage**: set app monitoring policies
#### Information protection
- Apply sensitivity label
- Block download to unmanaged device
- Remove external collab on confidential files
#### SSPM
Identifies misconfigurations, recommends actions > improve security posture
#### Advanced threat protection
Multi-modal sophisticated attacks

Typically starts with email, then moves laterally to compromise endpoints and identities > access in-app data

Built-in AAC (Adaptive Access Control), UEBA (User and Entity Behavior Analysis)

#### App to app protection
OAuth: open standard for token-based authentication and authorization, 3rd party services can use user account info without compromising password

App governance protects inter-app data exchange