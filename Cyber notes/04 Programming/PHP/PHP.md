"**;**" always ends a PHP declaration

#### Variables
are declared with "**$**"
```php
$my_variable = "a string";
```

Can be string, integer, float, boolean, null (NULL)

##### String
Similar to f-strings:
```php
$second_part = "the 2nd part of the string"
$composed_string = "The 1st part of the string, {$second_part} and the 3rd part"
```
or
```php
$second_part = "the 2nd part of the string"
$composed_string = "The 1st part of the string" . $second_part . "and the 3rd part"
```

##### Array
```php
$my_array = array(
	"key1" => "value1", 
	"key2" => "value2");
```
or
```php
$my_array = [
	"key1" => "value1",
	"key2" => "value2"
];
```
***Keys** can be str or int, **values** can be any type*

Values can be accessed like this
```php
$value1 = $my_array[key1];
```

#### Conditions
##### if, elif, else
```php
<?php  
if (logical condition 1) {  
action to be performed if logical condition 1 is met;  
} elseif (logical condition 2) {  
action 2;  
} else {  
action for everything else;  
}  
?>
```

##### Comparison operators

**`==`** or **`===`**: equal or identical (also same type)
**`!=`** or **`<>`** (SQL and older languages): not equal
**`!==`**: not identical
**`<`**, **`>`**: lower than, greater than
**`<=`**, **`=>`**: lower/greater or equal
**`$x <=> $y`**: "*spaceship*", returns -1 if $x < $y, 1 if $x > $y, 0 if $x = $y

##### Logical operators

**`$a and $b`** or **`$a && $b`**: and
**`$a or $b`** or **`$a || $b`**: or
**`$a xor $b`**: either or, not both
**`not $a`** or **`!$a`**: not

##### Inside HTML code
```php
<html>
    <head><title>Hi!</title></head>
    <body>
        <?php if (isset($_GET['name'])){ ?>
            <h1>Hello <?php echo $_GET['name']; ?>!</h1>
        <?php } else { ?>
            <h1>Hello nobody!</h1>
        <?php } ?>
    </body>
</html>
```
- **`$_GET`**: *superglobal array that contains data sent in URL query string*
- **`isset()`**: *checks if variable is set and is not `null`*

So, if a variable "name" is not "null" in the URL query string, H1 is "*Hello \[content of the variable "name"]!*"

For instance, if I go to "http://localhost/test-website/index.php?name=Incelticide", H1 = "Hello Incelticide"; if I go to "http://localhost/test-website/index.php", H1 = "Hello nobody!"

##### Switch
*used only to test equality*
```php
switch ($variable0) {
	case "$variable1":
		# command1 to be executed if $variable0 == $variable1;
		break; # prevents from executing command2 and 3
	case "$variable2":
	case "$variable3":
		# command2, to be executed if $variable0 == $variable2 or $variable0 == $variable 3;
		break; # prevents from executing command 0
	default:
		# command0 to be executed else
}
```

##### Ternary operator
*shorter if/else loop*

```php
(condition) ? $value_if_true : $value_if_false ;
// usually assigned to a variable:
$result = condition ? $value_if_true : $value_if_false ;
```

Practical example: getting values of text fields from a form
```php
if (isset($_POST['submit'])) { 
	$name = isset($_POST['name']) ? $_POST['name'] : null;
	$email = isset($_POST['email']) ? $_POST['email'] : null;
}
```

###### Shorthand/Elvis operator
*even shorter version of Ternary operator*
```php
$val = isset($_GET['user']) ? $_GET['user'] : 'default';
// can be shortened into
$val = $_GET['user'] ?: 'default';
```

#### Docstrings
```php
// This is a comment on one line
# This is another comment on one line

/* This is a comment
on several lines */
```

#### Functions

```php
function my_function($argument1, ...) {
	return $my_result;
}
```
