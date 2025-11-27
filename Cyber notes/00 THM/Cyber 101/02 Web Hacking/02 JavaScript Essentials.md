https://tryhackme.com/room/javascriptessentials

### Table of contents
- [[#Essentials]]
- [[#Integration with HTML]]
	- [[#Internal JS]]
	- [[#External JS]]
- [[#Dialogue Functions]]
- [[#Control Flow Statements]]


___
### Essentials
[[#Table of contents|Back to the top]]

3 ways to declare a **variable**
- **`var`**: function-scoped - accessible within function it was declared in
- **`let`**, **`const`**: block-scoped - only available within block delimited by `{ }`
  `let` allows variable to be reassigned, `const`doesn't

**Data types**: string, number, boolean, null, undefined, object, ...

**Function**
```JS
<scipt>
	function MyFunction(myParameter) {
		// code that makes the function do what it is supposed to do;
	}
</script>
```

**Loops**: `for`, `while`, `do...while`
```JS
<script>
	for (let i = 0; i < 100; i++) {
		MyFunction(rollNumbers[i]);
	}
</script>
```

Use browser console to practice JS (`CTRL + MAJ + I`)

___
### Integration with HTML
#### Internal JS
[[#Table of contents|Back to the top]]

*Embedding JS code directly within HTML document*

Script inserted between `<script>` tags, typically placed inside `<head>` section or inside `<body>` section

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Internal JS</title>
</head>
<body>
    <h1>Addition of Two Numbers</h1>
    <p id="result"></p>

    <script>
        let x = 5;
        let y = 10;
        let result = x + y;
        document.getElementById("result").innerHTML = "X + Y = " + result;
    </script>
</body>
</html>
```
*`document.getElementById("result").innerHTML` selects an element and updated its content*

#### External JS
[[#Table of contents|Back to the top]]

*JS code is imported from separated .js file*

script.js
```JS
let x = 5;
let y = 10;
let result = x + y;
document.getElementById("result").innerHTML = "The result is: " + result;
```
external.html
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>External JS</title>
</head>
<body>
    <h1>Addition of Two Numbers</h1>
    <p id="result"></p>

    <!-- Link to the external JS file -->
    <script src="script.js"></script>
</body>
</html>
```
*`<script src="script.js"></script>` imports the JS script from the .js file*

When pentesting, it's useful to identify whether the JS is internal or external. Some external JS might be unsafe and vulnerable.

___
### Dialogue Functions
[[#Table of contents|Back to the top]]

--> `alert`, `prompt`, `confirm`: display messages, gather input, obtain user confirmation
Can be exploited for XSS

```JS
// Ask user for name and confirmation
let userName;
let userConfirmation;
userName = prompt("What is your name?");
userConfirmation = confirm("Are you sure?");

// Repeat until user confirms name
while (userConfirmation == false) {
    userName = prompt("What is your actual name?");
    userConfirmation = confirm("Are you sure " + userName + " is your name?");
}

// Greet user with confirmed name
alert("Hello " + userName);
```


___
### Control Flow Statements
[[#Table of contents|Back to the top]]

Control flow: order in which statements and blocks are executed based on conditions

Conditional Statements
`if-else`
```JS
if (condition) {
	// action to be completed if condition returns true
} else {
	// action to be completed if condition returns false
}
```


___
### Minification
[[#Table of contents|Back to the top]]

*Compressed in JS*

Removes unnecessary characters: spaces, line breaks, comments, shortens variable names.
Reduces file size, improves loading time of web pages

// Obfuscation: make code harder to understand

___
### Best practices
[[#Table of contents|Back to the top]]

- Avoid client-side validation only. Client can disable/manipulate JS --> validate server-side too

- Trusted libraries only (`src`)

- No hardcoded secrets: API keys, access tokens, credentials, ...

- Minify and obfuscate: reduce size, improve loading time, make it harder for attacker to understand logic
