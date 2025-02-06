*Interesting to learn more about PHP because it's a **big attack vector** (SQL injections, reverse shell attack, ...) and people are not super into it so not many people are super skilled in it*

"**;**" always ends a PHP declaration

- [[#Variables]]
- [[#Conditions]]
- [[#Functions]]
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
# or
$my_array = [
	"key1" => "value1",
	"key2" => "value2"
];
# or
$my_array = ["value1", "value2"] // $my_array[0] = "value1"
```
***Keys** can be str or int, **values** can be any type (including other arrays)*

Values can be accessed like this
```php
$value1 = $my_array[key1];
```

###### Array manipulations
```php
// display content of array
var_dump($my_array)
print_r($my_array) # less info

// add element to array
array_push($my_array, $element)
$my_array[] = $element
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

#### Loops

##### foreach
```php
foreach ($my_array as $value) {
	# action to be performed for each element of the array
}
```

##### while
```php
while (condition) {
	# action to be performed if condition satisfied
}
```

##### for
```php
for (expr1; expr2; expr3) {
	# statement
}
```
- `expr1`: initializes loop
- `expr2`: is evaluated at each iteration, if true `statement` is executed
- `expr3`: is performed at the end of each iteration

Example
```php
for ($i = 1; $i <= 10; $i++) {
	echo $i
}
```
- `$i = 1`: loop starts with $i = 1
- `$i <= 10`: as long as $i is lower or equal to 10, $i is printed
- `$i++`: at the end of each iteration $i is incremented by 1
	*$\Rightarrow$ Loop prints numbers from 1 to 10*

#### Functions

```php
function my_function($argument1, ...) {
	return $my_result;
}
```

#### Docstrings
```php
// This is a comment on one line
# This is another comment on one line

/* This is a comment
on several lines */
```
___

### Forms

#### GET & POST

Used to send and retrieve information collected in a form

```php
<html>
    <head>
        <title>Form</title>
    </head>
    <body>
        <form action="index.php" method="get">
            <label>username</label><br>
            <input type="text" name="username"><br>
            <label>password</label><br>
            <input type="password" name="password"><br>
            <input type="submit" value="submit">
        </form>
    </body>
</html>

<?php
if ( isset( $_GET["username"] ) ) {
    echo "{$_GET["username"]}<br>";
}
if ( isset( $_GET["password"] ) ) {
    echo "{$_GET["password"]}<br>";
}
?>
```

**Data is appended to URL**: http://localhost/exos/index.php?username=my_username&password=my_password

Client can modify variables in URL as they wish $\Rightarrow$ less secure

GET requests can be cached while POST cannot

**$\Rightarrow$** **GET** can be more appropriate for a ***search page***

**$\Rightarrow$** Use **POST** method (more secure) for sensitive information such as ***credentials***

**`$_GET`** and **`$_POST`** are ***supervariables***: ***arrays*** storing other variables

>In the above example, the ***keys*** of the array are the ***names*** we gave to each input ("username" and "password") and the ***values*** are whatever ***input*** the client entered.

#### Data processing

1. Sanitization
2. Validation
3. Execution
4. Display/Redirection

##### 1. Sanitization
*Prevent toxic data from contaminating system*

```php
$sanitized_data = filter_var($_POST["input_data"], FILTER_SANITIZE_DATA);
```

`filter_var` function removes/encodes unwanted characters from `$_POST["input_data"]` using filter `FILTER_SANITIZE_DATA`

**[Sanitizing filters list](https://www.php.net/manual/en/filter.constants.php#constant.filter-sanitize-string)**

##### 2. Validation
*Ensures data has valid format (string, int, email, IP, ...)*

```php
$validation = filter_var($sanitized_data, FILTER_VALIDATE_DATA);
```

**[Validation filters list](https://www.php.net/manual/en/filter.constants.php#constant.filter-validate-bool)**

#### 3. Execution
*Add sanitized and validated data to database*

##### 4. Display/Redirection
*Indicate success or redirect to another page*


Sanitization $\rightarrow$ Display/Redirection, full example:
```php
<?php
// Step 1: Sanitization
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize input data
    $sanitized_email = filter_var($_POST["email"], FILTER_SANITIZE_EMAIL);

    // Step 2: Validation
    if (filter_var($sanitized_email, FILTER_VALIDATE_EMAIL) === false) {
        echo "Invalid email address. Please try again.";
        exit();
    }

    // Step 3: Execution (Adding to the database)
    try {
        // Database connection
        $pdo = new PDO('mysql:host=localhost;dbname=test', 'username', 'password');
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Use prepared statements to safely insert data
        $stmt = $pdo->prepare("INSERT INTO users (email) VALUES (:email)");
        $stmt->bindParam(':email', $sanitized_email);

        // Execute the query
        if ($stmt->execute()) {
            // Step 4: Display/Redirection
            echo "Registration successful!";
            header("Location: success.php");
            exit();
        } else {
            echo "An error occurred while saving your data. Please try again.";
        }
    } catch (PDOException $e) {
        // Handle database connection or query errors
        echo "Database error: " . htmlspecialchars($e->getMessage());
    }
} else {
    // If the request method is not POST, show the registration form
?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Registration</title>
    </head>
    <body>
        <h2>User Registration</h2>
        <form method="POST" action="">
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" required>
            <button type="submit">Register</button>
        </form>
    </body>
    </html>
<?php
}
?>
```
