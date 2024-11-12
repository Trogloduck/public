`#!/bin/bash`: 1st line of a shell script, called "sha-bang", "/bin/bash" is the path where the shell interpreter is located

`which bash`: used to find the path for the above line

.sh: common extension for shell scripts

`#`: used to comment

___
Variables can be declared like so

```bash
variable1=number
Variable_2="another number"
VARIABLE3=5
```

They can be called like so

```bash
echo "My number is $variable1"
echo "Another way to display ${variable1}"
```

Substitution: assigning a command to a variable, using \`command\`

```
filelist=`ls`
```

___
my_script.sh:

```bash
#!/bin/bash
echo "File name: "$0
echo "1st argument: "$1
data=$2
echo "2nd argument: "$data
echo $#
```

Arguments can be passed in my_script.sh:

`my_script.sh argument1 argument2 argument3`

`$0` references the script itself

`$1` references the 1st argument, and so on

Output: 

```
File name: my_script.sh
1st argument: argument1
2nd argument: argument2
2
```

___
Arrays: works similarly to lists in Python but with parentheses and without commas

```bash
my_array=(apple banana "Fruit Basket" orange)
new_array[2]=apricot
```

`${#arrayname[@]}`: total number of elements in the array

Example:

```bash
echo ${my_array[${#my_array[@]}-1]}
```
*will find the total number of elements in the array, subtract 1, find and print the element corresponding to that index (the last element of the array)*

___
Basic operations:

```bash
A=3
B=$((100 * $A + 5)) # 305
```

Basic string operations:

```bash
STRING="this is a string"
echo ${#STRING}            # 16
```

Index

```bash
#       1234567890123456
STRING="this is a string"
SUBSTRING="hat"
result=$(expr index "$STRING" "$SUBSTRING")     # 1 is the position of the first 't' in $STRING
```

Substring extraction

```bash
STRING="this is a string"
POS=1
LEN=3
echo ${STRING:$POS:$LEN}   # his
```
If `$LEN` omitted, prints until the end

