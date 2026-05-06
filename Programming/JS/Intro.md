`console.log()`: outputs information to console (part of web browser used for debugging)

`//`: comment

### Variables

Data types
- Integer, float, string, boolean
- **`undefined`:** declared variable without value yet
- **`null`:** variable set to nothing
- **Object:** collection of key-value pairs
```JS
{
  name: "Alice",
  age: 30
};
```
- **Symbols:** unique and unchangeable, often used to create labels/identifiers
```js
Symbol('mySymbol');
```
- **BigInt:** large numbers, exceeding limit of `Number` type
```JS
1234567890123456789012345678901234567890n;
```
*Create `BigInt` by `n` at the end*

### Declare Variable

**`let`**

```js
let age;
console.log(age); // undefined
```

```js
let age = 25;
console.log(age); // 25

age = 30;
console.log(age); // 30
```

>Variables can start with letter, `_`, `$`, **can't start with a number**

Case-sensitive

Naming convention: camelCase

**`const`:** used to declare variable that won't change value (trying to change would result in error), can't be `undefined` 

Avoid using `var`: deprecated