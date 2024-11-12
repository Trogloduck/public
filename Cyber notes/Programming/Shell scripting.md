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

Substitution: assigning a command to a variable. For instance, 

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
Arrays:

```bash
my_array=(apple banana "Fruit Basket" orange)
new_array[2]=apricot
```

