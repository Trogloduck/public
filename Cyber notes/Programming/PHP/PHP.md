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
  0 => 'item1', 
  1 => 'item2', 
  2 => 'item3');
```

#### Conditions
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

##### Inside HTML code
```php
<html>
    <head><title>Hi!</title></head>
    <body>
        <?php if (isset($_GET['name'])){ ?>
            <h1>Hello <?php echo $_GET['name']; ?>!</h1>
        <?php } else { ?>
            <h1>Hello nobody</h1>
        <?php } ?>
    </body>
</html>
```
- **`$_GET`**: *superglobal array that contains data sent in URL query string*
- **`isset()`**: *checks if variable is set and is not `null`.*

So, if a variable "name" is not "null" in the URL query string, H1 is "*Hello \[content of the variable "name"]!*"

For instance, if I go to "http://localhost/test-website/index.php?name=Incelticide", H1 = "Hello Incelticide"

