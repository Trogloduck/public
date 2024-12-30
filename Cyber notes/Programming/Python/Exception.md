#### try - except
*allow to handle different types of exceptions*

```python
try:
	3 / 0
except ZeroDivisionError:
	print("Error: You can't divide by zero")
except ValueError:
	print("Error: Non-numeric value")
except BaseException:
	print("Error: there is a problem")
```

*This case will return the ZeroDivisionError exception*

```python
try:
	3 / int("a")
```
*would return the ValueError exception*

#### else
*can be used to signify no exception was triggered*

```python
try:
	...
except:
	...
else:
	print("No exception triggered")
```

#### finally
*executes after all previous blocks no matter what*

#### raise
*can be used to artificially trigger an error*

```python
def division(num, div):
	if div == 0:
		raise ZeroDivisionError("Division by zero is impossible")
	else:
		return num/div
```

#### class
*can be used to create custom exceptions*

```python
class MyCustomException(Exception):
	def __init__(self, variable):
		super().__init__(message)
		self.variable = variable
		self.message = f"Variable cannot have this value: variable = {variable}"
```

