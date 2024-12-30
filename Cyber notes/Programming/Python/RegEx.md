A regular expression describes a way to search a string for a pattern
- Position
- Set of characters
- Quantifier

**Position**
- `^`: `^a` *matches strings that start with an* `a`
- `$`: `z$` *matches strings that end with a* `z`

**Set of characters**
- `[aeiou]`: *matches strings containing 1 vowel* (brackets allow to create custom set of characters)
- `\d`: *matches strings containing 1 **digit***
- `\d\d`: *matches 2 consecutive digits*
- `\s`**pace***
- `\w`**ord character**: *matches `a-z`, `A-Z`, `0-9`, `_`*

**Quantifier**
- `[aeiou]{x}`: *matches strings containing x consecutive vowels*