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