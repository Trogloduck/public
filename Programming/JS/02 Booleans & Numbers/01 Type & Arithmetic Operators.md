##### Type

All under type **`Number`** whether **integer**, **float** or even **infinity** (x/0 | x =!= 0)
**`NaN`** happens when trying to apply **mathematical** operation to **non number** type, `NaN`'s type is still `Number`

___
##### Operators

**`+`**, **`-`**, **`*`**, **`/`**

**`%`:** modulo (returns remainder)
e.g. : `10 % 3 = 1`

**`**`:** exponentiation

___
##### Numbers + Strings

**`+`**
**Type coercion** to string --> **concatenation**
e.g. : `5 + '10' = 510`

**`-`**, **`*`**, **`/`**
- **Type coercion** to number if possible (e.g. : `'1' --> 1`)
- If not possible --> `NaN` (e.g. : `'abc'`)
- `true --> 1`, `false --> 0`
- `null --> 0`, `undefined --> NaN`

___
##### Incrementation / Decrementation

Prefix/Postfix
```JS
// Prefix incrementation
let x = 5
console.log(++x) // 6
console.log(x) // 6

//Postfix decrementation
x = 5
console.log(x--) // 5
console.log(x) //4
```

