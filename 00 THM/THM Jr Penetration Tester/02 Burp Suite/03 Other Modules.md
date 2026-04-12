https://tryhackme.com/room/burpsuiteom

### Table of contents
- [[#Decoder]]
- [[#Comparer]]
- [[#Sequencer]]
- [[#Organizer]]

___
### Decoder
[[#Table of contents|Back to the top]]

*Like an integrated **Cyberchef**, **encode** and **decode***

#### Encode
- **URL:** safe transfer of data in URL, substitute characters for **ASCII** code in **hexadecimal** format preceded by "**`%`**"
- **HTML:** **escapes special characters** by replacing them with "**`&`**" followed by hexadecimal / reference ending with "**`;`**", ensures safe rendering of special characters in HTML, prevents XSS
- **Base64:** converts any data into **ASCII compatible** format
- **ASCII hex:** converts data between **ASCII** and **hexadecimal**
- **Hex**, **Octal**, **Binary**: only apply to numbers
- **Gzip:** compress

**Hex format:** can be useful when needing to **view and edit data byte-by-byte**

**Hashing:** hash > ASCII hex

___
### Comparer
[[#Table of contents|Back to the top]]

*Compare 2 pieces of data by **ASCII words** or **bytes***

- [ ] ***Sync views***
Ensures if one set of data changes format (into hex for instance), other set follows

--> Brute-force/stuffing attack: compare responses with different length to see where difference lies between successful and failed authentication

Typical workflow
1. **Capture** request in Proxy, send to Repeater
2. **Send** request in **Repeater**, send response to **Comparer**
3. **Modify** request and **send** it, send response to **Comparer**

___
### Sequencer
[[#Table of contents|Back to the top]]

*Evaluate **entropy** ("randomness") of **tokens***

- **Live capture:** pass request that will generate token to Sequencer for analysis (for instance, POST request to login endpoint)
  Sequencer can make same requests thousands of times, storing sample tokens in order to analyze predictability
- **Manual load:** load list of pre-generated tokens, no need for requests to be made

Results
- **Overall result**: broad assessment
- **Effective entropy**: tokens randomness measure
- **Reliability**: significance level
- **Sample**: details about token samples analyzed

___
### Organizer
[[#Table of contents|Back to the top]]

***Store**, **annotate** copies of HTTP **requests**, read only*

`CTRL + O`