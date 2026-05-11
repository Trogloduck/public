### ASCII

**`.charCodeat()`**

```js
let letter = "A";
console.log(letter.charCodeAt(0));  // 65
```
*from Unicode (UTF-16) to ASCII*

**`.fromCharCode()`**

```js
let char = String.fromCharCode(65);
console.log(char);  //  A
```
*from ASCII to UTF-16*

### Finding

**`.includes()`**

```js
string.includes(searchValue);
```
*returns true if string contains searchValue (false if it doesn't)*

### Extracting

**`.slice()`**

```js
string.slice(startIndex, endIndex);
string.slice(startIndex); // till the end
string.slice(-endIndex); // from the end
```
*doesn't include letter corresponding to endIndex*

