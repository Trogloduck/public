```JS
let example = "Example string value";
```
*Can be declared with either single or double quotes*

##### Concatenation

>**`+`**
```js
let firstName = "John";
let lastName = "Doe";

let fullName = firstName + " " + lastName; 
console.log(fullName); // John Doe
```
*simple concatenation*

>**`+=`**
```js
let greeting = 'Hello';
greeting += ', John!';

console.log(greeting); // "Hello, John!"
```
*building string step by step, appending new content to existing string*

>**`.concat()`**
```js
let str1 = 'Hello';
let str2 = 'World';

let result = str1.concat(' ', str2); 
console.log(result); // Hello World
```
*concatenate multiple strings*

**Newline: `\n`**

**Escaping character: `\`**
e.g. : `let statement = "She said, \"Hello!\"";`

##### Bracket Notation

```js
let greeting = "hello";
console.log(greeting[greeting.length - 1]); // "o"
```

##### Template Literals

```JS
let name = "Bob";
let greeting = `Hello, ${name}!`;
```
*Like an f-string in Python*

Can be used for multiple line strings (--> doesn't require "\n")

```js
const song = "Bohemian Rhapsody";
const score = 9.5;
const highestScore = 10;
const output = `One of my favorite songs is "${song}". I rated it ${
  (score / highestScore) * 100
}%.`;
```
*Can also be used to integrate JS expressions*

##### `.indexOf()`

```js
let sentence = "JavaScript is awesome!";
let position = sentence.indexOf("awesome!");
console.log(position); // 14
```
If substring isn't found --> "-1"

##### `prompt()`

Display pop-up prompting user for input

```js
prompt(message, default);
```
- `message`: message prompting user for input
- `default`: default value in input field

