< [[10 Python]]

**Indentation**: *4 spaces* > tab (displayed the same across editors)

**Code layout**: include \\n between functions, use """ to explain what a function does, when dealing with many parameters declaring them across several lines:
```
def my_function(parameter):
	"""
	What the function does
	"""
	pass

def many_parameters(
	param1, param2, param3, param4, param5,
	param6, param7, param8, param9, param10
):
	"""
	Perform an operation with the given parameters.
	Parameters:
	- param1 (type): Description of param1.
	- param2 (type): Description of param2.
	- ...
	- param10 (type): Description of param10.
	- """
	pass
```

**Import**: at the beginning of code, one line per import, 1st internal modules \\n, then 3rd party libraries \\n, then own modules

**Spaces**: *operators* surrounded by spaces
***Exceptions***: 
Showing ***mathematical priority***: `b = x*x + y*y`
 "=" used for ***parameter declaration***: `def my_function(parameter='value'):`
 or ***argument passing***: `my_function(arg='value')`

**Naming conventions**: *snake_case* (my_variable, my_function, my_module), *PascalCase*(MyClass)