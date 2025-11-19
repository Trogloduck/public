```YAML
title: AnyDesk Installation
status: experimental
description: AnyDesk Remote Desktop installation can be used by attacker to gain remote access.
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    CommandLine|contains|all:
      - '--install'
      - '--start-with-win'
    CurrentDirectory|contains:
      - 'C:\ProgramData\AnyDesk.exe'
  condition: selection
falsepositives:
- Legitimate deployment of AnyDesk
level: high
references:
- https://twitter.com/TheDFIRReport/status/1423361119926816776?s=20
tags:
- attack.command_and_control
- attack.t1219
```
