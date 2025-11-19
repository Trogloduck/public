*Yet Another Random Acronym*

### Table of contents
- [[#Intro]]
- [[#YARA rules]]
- [[#YARA Modules]]
- [[#Other Tools]]

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
```yaml
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

[Yara writing rules](https://yara.readthedocs.io/en/stable/writingrules.html)

#### Meta
`desc`acts like `#`: docstring explaining rule

#### `strings`
```yaml
rule helloworld_checker {
	strings:
		$hello_world = "Hello World!"
	
	condition:
		$hello_world
}
```
Define strings we want to search, make it the condition $\rightarrow$ create a match if file **contains** "Hello World!"

```yaml
rule helloworld_checker{
	strings:
		$hello_world = "Hello World!"
		$hello_world_lowercase = "hello world"
		$hello_world_uppercase = "HELLO WORLD"

	condition:
		any of them
}
```
$\rightarrow$ create match if file contains **any** of the variations of the string

#### Conditions
Can use mathematical operators: `<`, `>`, `<=`, `>=`, `==`, `!=`

```yaml
rule helloworld_checker{
	strings:
		$hello_world = "Hello World!"

	condition:
        #hello_world <= 10
}
```
$\rightarrow$ create a match if file has **10 or less** occurrences of `$hello_world`

#### Combining keywords
`and`, `not`, `or`

```yaml
rule helloworld_checker{
	strings:
		$hello_world = "Hello World!" 
        
    condition:
	    $hello_world and filesize < 10KB 
}
```

![[Pasted image 20250328093537.png]]
https://blog.securitybreak.io/security-infographics-9c4d3bd891ef#18dd

___
### YARA Modules
[[#Table of contents|Back to the top]]
#### Cuckoo Sandbox
Automated malware analysis environment $\rightarrow$ generate yara rules based on behavior observed in Cuckoo Sandbox

#### Python PE
Create Yara rules from sections/elements of Windows Portable Executable structure (standard formatting for executables and DLLs)
Examining PE file's content important: cryptography, worming easily identified

___
### Other Tools
[[#Table of contents|Back to the top]]

**[Awesome YARA](https://github.com/InQuest/awesome-yara)**: curated yara rules list

**[LOKI](https://github.com/Neo23x0/Loki)**: free open-source IOC scanner
1. File Name IOC Check
2. **Yara** Rule Check
   Run LOKI from within directory with file to analyze: `python PATH/TO/loki.py -p .`
3. Hash Check
4. C2 Back Connect Check

**[THOR Lite](https://www.nextron-systems.com/thor-lite/)**: IOC and YARA scanner

**[FENRIR](https://github.com/Neo23x0/Fenrir)** : same as 2 above but **Bash script $\rightarrow$ no requirements**

**[YAYA](https://github.com/EFForg/yaya)** -- Yet Another YARA Automation: **manage** multiple yara rule repositories (Linux only)

**[yarGen](https://github.com/Neo23x0/yarGen)**: yara rule generator, include strings found in malware files, exclude strings and opcodes found in goodware files
Run from within yarGen directory: `python3 yarGen.py -m PATH/TO/target_file --excludegood -o PATH/TO/output.yar`

**[yarAnalyzer](https://github.com/Neo23x0/yarAnalyzer/)**: yara rule analyzer and statistics

**[Valhalla](https://valhalla.nextron-systems.com/)**: rich yara rule database