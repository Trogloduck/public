*Yet Another Random Acronym*

### Table of contents
- [[#Intro]]
- [[#YARA rules]]

___
### Intro
[[#Table of contents|Back to the top]]

_Pattern matching swiss knife for malware researchers_

Binary and text patterns

Malware store some data in strings that can be used in yara rules to detect malware patterns

Examples of strings: Bitcoin wallet, IP of C2

___
### YARA rules
[[#Table of contents|Back to the top]]

2 arguments: rule file, name of file/directory/ process ID to use rule for

`my_rule.yar`
```YARA
rule my_rule {
	condition: true
}
```

```Bash
yara my_rule.yar my_directory
```
- Uses yara rule `my_rule.yar`on `my_directory`
- If `my_directory` exists, output: `my_rule my_directory`
- If not, output: `error scanning non_existant_file: could not open file`

