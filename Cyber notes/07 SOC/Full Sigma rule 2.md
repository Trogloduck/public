```YAML
title: Detection of Ransomware Activity via Scheduled Task Creating .txt File
status: experimental
description: Detects a suspicious scheduled task (process creation) where cmd.exe creates a .txt file, possibly indicative of ransomware activity.
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    Image|endswith: \cmd.exe
    CommandLine|contains: 
      - '.txt'
      - '>'
      - 'type nul >'
    User: 
      not: 'SYSTEM'
  condition: selection
falsepositives:
  - Legitimate administrative scripts creating text files.
level: high
```
