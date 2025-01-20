"**;**" always ends a PHP declaration

#### Variables
are declared with "**$**"
```php
$my_variable = "a string";
```

Can be string, integer, float, boolean, null (NULL)

**Array**
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

#### Docstrings
```php
// This is a comment on one line
# This is another comment on one line

/* This is a comment
on several lines */
```

resume at drill exercices
