eXtensible Markup Language

Used to encode documents in a format that is both human- and machine-readable, used to store and transport data

1. **Platform-independent and programming language independent**
2. Data stored and transported using XML can be changed at any point in time without affecting data presentation
3. **Validation** using DTD and Schema (document is free from any syntax error)
4. **No conversion needed** when transporting data between multiple systems


```XML
<?xml version="1.0" encoding="UTF-8"?>
<mail>  
   <to>falcon</to>  
   <from>feast</from>  
   <subject>About XXE</subject>  
   <text>Teach about XXE</text>  
</mail>
```
1st line is the prolog
Then `<mail>` is the ROOT element, `<to>`, `<from>`, `<subject>`, `<text>` are children elements

XML is case-sensitive

Attributes can be used like in HTML
```XML
<text category = "message">You need to learn about XXE</text>
```
`category` is the attribute name, `message` is the attribute value

##### DTD

Document Type Definition, defines structure and legal elements and attributes of an XML document

`note.dtd`
```DTD
<!DOCTYPE note [ <!ELEMENT note (to,from,heading,body)> <!ELEMENT to (#PCDATA)> <!ELEMENT from (#PCDATA)> <!ELEMENT heading (#PCDATA)> <!ELEMENT body (#PCDATA)> ]>
```
*#PCDATA means parseable character data*

This DTD can be used to validate information of some XML

```XML
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE note SYSTEM "note.dtd">  
<note>  
    <to>falcon</to>  
    <from>feast</from>  
    <heading>hacking</heading>  
    <body>XXE attack</body>  
</note>
```
