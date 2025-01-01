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
- `\D`: *anything but digits*
- `\d\d`: *matches 2 consecutive digits*
- `\s`**pace***
- `\w`**ord character**: *matches `a-z`, `A-Z`, `0-9`, `_`*
- `\W`:                *anything but `a-z`, `A-Z`, `0-9`, `_`*

**Quantifier**
- `[aeiou]{x}`: *matches strings containing x consecutive vowels*
- `^\w{x}$`: *exactly x characters long strings*

#### Use

```python
import re

names = ['Finn Bindeballe',
        'Geir Anders Berge',
        'HappyCodingRobot',
        'Ron Cromberge',
        'Mikkel Christensen',
        'Sohil',
         ]

# Find people with first and last name only
regex = '^\w+ \w+$'

for name in names:
    result = re.search(regex, name)
    if result:
        print(result)
```

**`re.search`**: finds 1st string matching regex, returns *match object* containing *match* itself and *span*

- **`match.span`**: returns span (tuple, index of 1st and last characters of 1st string matching the regex)
	- **`match.start`**: returns start of span
	- **`match.end`**: returns end of span

**`re.findall`**: returns list of all strings matching regex

**`re.match`**: 

**Groups**

```python
regex = '^(\w+)\s+(\w+)$'

first_name = match.group(1)
last_name = match.group(2)
```

Possible to give a name to the groups within the regex

```python
regex = '^?P<first_name>(\w+)\s+?P<last_name>(\w+)$'

first_name = match.group('first_name')
last_name = match.group('last_name')
```

