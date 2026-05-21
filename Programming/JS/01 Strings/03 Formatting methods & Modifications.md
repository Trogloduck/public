##### Formatting

**`.toUpperCase()`** & **`.toLowerCase()`**
Converts all to upper/lower case

**`.trim()`:** remove **all** leading and trailing whitespace
**`.trimStart()`:** remove only **leading** whitespace
**`.trimEnd()`:** remove only **trailing** whitespace

___
##### Modifications

**`.replace()`**
```JS
string.replace(searchValue, newValue);
```
*replaces only 1st occurence*
`.replaceAll()` replaces all occurrences

**`.repeat()`**
```JS
string.repeat(count);
```

- Negative number, `Infinity` --> returns error
- Float --> round down to nearest int
- 0 --> empty string