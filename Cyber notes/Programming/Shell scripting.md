Table of content
- [Basics](#basics)
- [Variables](#variables)
- [Calling arguments](#calling-arguments)
- [Arrays](#arrays)
- [Basic operations](#basic-operations)
- [Decision making](#decision-making)
- [Loops](#loops)
- [Functions](#functions)
- [Monitoring commands](../../Monitoring%20and%20displaying%20project/Elements%20to%20monitor.md)
___
### Basics

`#!/bin/bash`: 1st line of a shell script, called "sha-bang", "/bin/bash" is the path where the shell interpreter is located

`which bash`: used to find the path for the above line

.sh: common extension for shell scripts

`#`: used to comment

___
### Variables
can be declared like so

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
### Calling arguments
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
### Arrays
works similarly to lists in Python but with parentheses and without commas

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
### Basic operations

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

Substring replacement

```bash
STRING="to be or not to be"
echo ${STRING[@]/be/eat}        # to eat or not to be
```
*replaces 1st occurrence*

```bash
STRING="to be or not to be"
echo ${STRING[@]//be/eat}        # to eat or not to eat
```
*replaces all occurrences*

```bash
STRING="to be or not to be"
echo ${STRING[@]// not/}        # to be or to be
```
*deletes all occurrences*

```bash
STRING="to be or not to be"
echo ${STRING[@]/#to be/eat now}    # eat now or not to be
```
*replaces occurrence if at beginning of $STRING*

```bash
STRING="to be or not to be"
echo ${STRING[@]/%be/eat}        # to be or not to eat
```
*replaces occurrence if at end of $STRING*

```bash
STRING="to be or not to be"
echo ${STRING[@]/%be/be on $(date +%Y-%m-%d)}    # to be or not to be on 2012-06-14
```
*replaces occurrence with shell command output*

___
### Decision making

```bash
if [ expression ]; then
  code that will execute if 'expression' is true
fi
```

```bash
NAME="John"
if [ "$NAME" = "John" ]; then
  echo "True - my name is indeed John"
fi
```

Else condition:
```bash
NAME="Bill"
if [ "$NAME" = "John" ]; then
  echo "True - my name is indeed John"
else
  echo "False"
  echo "You must mistaken me for $NAME"
fi
```

Elif condition:
```bash
NAME="George"
if [ "$NAME" = "John" ]; then
  echo "John Lennon"
elif [ "$NAME" = "George" ]; then
  echo "George Harrison"
else
  echo "This leaves us with Paul and Ringo"
fi
```

Numeric comparisons:

| $a **-lt** $b | $a **-gt** $b | $a **-le** $b | $a **-ge** $b | $a **-eq** $b | $a **-ne** $b |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| a \< b        | a \> b        | a $\leq$ b    | a $\geq$ b    | a = b         | a $\neq$ b    |

String comparisons:

| $a = $b            | $a == $b           | $a != $b              | -z "$variable" |
| ------------------ | ------------------ | --------------------- | -------------- |
| a is the same as b | a is the same as b | a is different from b | a is empty     |

Conditions can be combined:
```bash
if [[ $VAR_A[0] -eq 1 && ($VAR_B = "bee" || $VAR_T = "tee") ]] ; then
    command...
fi
```

___
### Loops

```bash
for arg in [list] ; do
 command(s)...
done
```
*runs command(s) for each arg in list*

```bash
while [ condition ] ; do
 command(s)...
done
```
*runs command(s) as long as condition is true*

```bash
until [ condition ] ; do
 command(s)...
done
```
*runs command(s) until condition is true (i.e. as long as condition is false)*

`break`and `continue` can be used in similar ways to Python

Conditions can be nested:
```bash
#!/bin/bash
# Enter your array comparison code here

a=(3 5 8 10 6)
b=(6 5 4 12)
c=(14 7 5 7)

# Selects the common element in all the lists

for number in "${a[@]}"; do
  in_b=false
  in_c=false
  for element in "${b[@]}"; do
    if [ "$number" -eq "$element" ]; then
      in_b=true
      break
    fi
  done
  for element in "${c[@]}"; do
    if [ "$number" -eq "$element" ]; then
      in_c=true
      break
    fi
  done
  if $in_b && $in_c; then
    echo $number
  fi
done
```

___
### Functions

```bash
function function_name {
  command...
}
```

___

