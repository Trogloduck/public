< [[04 Programming]]

Cascading Style Sheet
2 syntax styles, ruleset seems better overall

| Aspect                 | Ruleset Syntax                          | Inline Syntax                                  |
| ---------------------- | --------------------------------------- | ---------------------------------------------- |
| **Definition**         | Applies styles to *selected elements*   | Styles written directly *within HTML elements* |
| **Placement**          | External CSS files or `<style>` blocks  | Inside the `style` attribute of HTML tags      |
| **Usage Example**      | `.example {`<br>  `color: blue;`<br>`}` | `<div style="color: blue;">`                   |
| **Specificity**        | Lower specificity                       | Highest specificity                            |
| **Maintainability**    | Easier to maintain                      | Harder to maintain                             |
| **Reusability**        | High                                    | Low                                            |
| **Performance**        | Better, can be cached                   | Can negatively impact performance              |
| **Preferred Use Case** | Most styling needs                      | Quick, one-off changes                         |
| **Example Use Case**   | Styling multiple elements or pages      | Testing or dynamic styling                     |
![[Pasted image 20240910093308.png#center]]

Use ruleset in external CSS file, then call it inside the head of the HTML:
`<link href='style.css' rel='stylesheet'>`
If the style.css file isn't in the same folder, inform `path/style.css`

***Universal*** selector: `* {}`

***Class*** attribute selector: `.attribute {}`

Possible to add multiple class attributes in 1 HTML declaration: `class='attribute1 attribute2`

To select just one element, give it and id, call the ***id*** in CSS with `#id`

***Attribute*** selector: `tag[attribute(=value)] {}`
Ex: `a[href*='florence'] {}` *selects all links including the word 'florence'*

***Pseudo-class*** selector: modify appearance/functionality of element after user interaction
`tag:pseudo-class {}`

More specific ruleset (ex: `id`) overrides less specific (ex: `class`)

***Style elements from lowest to highest degree of specificity***: 
Type selectors (e.g., `div`), Class selectors (e.g., `.class`), Attribute selectors (e.g., `[type="text"]`), Pseudo-class selectors (e.g., `:hover`), ID selectors (e.g., `#id`), Inline styles (e.g., `style="color: red;"`)

Possible to ***chain selectors***: `tag.class{}`

***Descendant combinator***: select nested elements (such as elements of a list)
`.main-list li {}`

***Multiple selectors***: use ','
`tag,
.class {}`

`!important` overrides everything regardless of specificity:
```
p {  
  color: blue !important;  
}
```
___

**[Keep learning!](https://www.codecademy.com/enrolled/courses/learn-css)**

