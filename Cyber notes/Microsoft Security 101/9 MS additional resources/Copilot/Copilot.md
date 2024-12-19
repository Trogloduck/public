- **Investigate and remediate security threats**: gain incidents context, triage complex security alerts, generate actionable summaries, step-by-step response guidance
- **Build KQL (Kusto Query Language) queries / analyze suspicious scripts**: eliminate need to manually write query-language scripts or reverse engineer malware scripts with natural language translation to enable every team member to execute technical tasks
- **Understand risks and manage org's security posture**: get broad picture of environment with prioritized risks to improve posture
- **Troubleshoot IT issues**: synthesize relevant information rapidly and receive actionable insights to identify and resolve IT issues quickly
- **Define and manage security policies**: define new policy, cross-reference it with others for conflicts, summarize existing policies to manage complex organizational context quickly and easily
- **Configure secure lifecycle workflows**: build groups, set access parameters with step-by-step guidance to ensure seamless configuration to prevent security vulnerabilities
- **Develop reports for stakeholders**: get clear, concise report, summarizes context, environment, open issues, protective measures prepared for audience tone and language

In addition to LLM (Large Language Model) and NLP (Natural Language Processing), Copilot integrates with security-specific sources for more context > more relevancy
___

#### Terminology

- **Session**: a conversation, persistent context
- **Prompt**: user question/statement
- **Capability**: function Copilot uses to solve part of a problem
- **Plugin**: set of capabilities by particular resource
- **Orchestrator** (backend): Copilot’s system for composing capabilities together to answer a user’s prompt

Example: Copilot plugin to MS Defender XDR capabilities
- **Summarize incident**
- **Guided responses** (recommended actions)
- **Analyze scripts**
- **Generate KQL**
- **Generate incident reports**
___
#### Process flow

![[Pasted image 20241219105755.png]]
##### Process log

User can see what capability Copilot used to generate response
#### Effective prompt

- **Goal**: specific, security-related information that you need
- **Context**: why you need this information / how you'll use it
- **Expectations**: format / target audience you want the response tailored to
- **Source**: known information, data sources, plugins Copilot should use

![[Pasted image 20241219110224.png]]

- Be specific, clear, concise
- Iterate
- Provide context for Copilot to narrow down
- Give positive instructions >>> negative
- Directly address Copilot ("You")
___

#### Provisioning

- Need an Azure subscription
- Be an Azure owner/contributor

Recommended to provision within Security Copilot rather than through Azure portal

Select a number of SCUs (Security Compute Units) to be provisioned \[1, 100]

#### Set up default environment

Need to have Entra role Global admin / Security admin

Setup
- SCU capacity
- Data storage
- Where prompts are evaluated
- Logging audit data in Purview: can store admin/user actions, Copilot responses
- Org's data sharing yes/no
- Plugin settings
#### Role permissions

Roles grant varying levels of access to Copilot

Entra roles
- Global admin: owner
- Security admin: owner
- Security operator: read/write
- Security reader: read only

Sec Copilot roles
- Copilot owner
- Copilot contributor: read/write

Can make role assignments
- Global admin
- Security admin
- Copilot owner

<html>
<head>
    <title>Role Access Summary</title>
</head>
<body>
    <table border="1">
        <thead>
            <tr>
                <th colspan="2" style="vertical-align: middle; text-align: center">Entra Roles</th>
                <th colspan="2" style="vertical-align: middle; text-align: center">Sec Copilot Roles</th>
                <th rowspan="2" style="vertical-align: middle; text-align: center">Can Make Role Assignments</th>
            </tr>
            <tr>
                <th style="vertical-align: middle; text-align: center">Role</th>
                <th style="vertical-align: middle; text-align: center">Access Level</th>
                <th style="vertical-align: middle; text-align: center">Role</th>
                <th style="vertical-align: middle; text-align: center">Access Level</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Global Admin</td>
                <td>Owner</td>
                <td rowspan="2" colspan="2" style="vertical-align: middle; text-align: center">Copilot Owner</td>
                <td>Global Admin</td>
            </tr>
            <tr>
                <td>Security Admin</td>
                <td>Owner</td>
                <td>Security Admin</td>
            </tr>
            <tr>
                <td>Security Operator</td>
                <td>Read/Write</td>
				<td>Copilot Contributor</td>
                <td>Read/Write</td>
                <td>Copilot Owner</td>
            </tr>
            <tr>
                <td>Security Reader</td>
                <td>Read Only</td>
                <td colspan="3"></td>
            </tr>
        </tbody>
    </table>
</body>
</html>



