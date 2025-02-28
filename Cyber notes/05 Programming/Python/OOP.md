< [[Python]]

- [Class]([[#**Class** defines *attributes* and *methods* related to *objects* of that class]])
- [Encapsulation]([[#**Encapsulation** limit access to variables and methods within a class]])
- [Inheritance]([[#**Inheritance** building a class from an already existing one]])
- [Static method]([[#**Static method** method with no access to other elements in the class]])
___
##### **Class**: defines *attributes* and *methods* related to *objects* of that class

```python
class Object:
	def __init__(self):
		self.name = "an object"
```
*All objects of this class will have the name "*`an object`*"*

`__init__` initializes the object
`self.name`: `self` refers to the object, `.name`is a method assigning a name to the object

`__init__`can take several parameters:
```python
class Object:	
	def __init__(self, name, shape, size):
		self.name = name
		self.shape = shape
		self.size = size
```

*When creating an object, we use those parameters to give specific attributes to the object:*
`dice = Object("dice", "cubic", "small")`

*We can then call for each parameters using the corresponding method:*
`dice.name`, `dice.shape`, `dice.size`

*\#docstrings that explain what the class/method does can be called by using* `help(Object)` */* `help(Object.method)`

`dir(Object)` returns *list* of *everything* in the object
`Object.__dir__` returns a *dictionary*, with *names* of attributes and methods as keys and their values as *values*
___
##### **Encapsulation**: limit access to variables and methods within a class

***Public***: default, anything goes

***Protected***: `_variable`,  `_method`; just a *convention*, won't actually lock

***Private***: `__variable`, `__method`; *locks*

*In the example of the class Object, I would have an attribute*
`self.nature = "physical"`
*and make it inaccessible by declaring it like this:*
`__self.nature = "physical"`

*Adding* `__` *is "called name mangling"*
___
##### **Inheritance**: building a class from an already existing one

Sub/derived/child has access to attributes and methods of super/base/parent

Ex:
Super class
```python
class Super:
    def __init__(self, super_attribute):
        self.super_attribute = super_attribute
```

Sub class
```python
class Sub(Super):

    def __init__(self, super_attribute, sub_attribute):
        Super.__init__(self, super_attribute)
        self.sub_attribute = sub_attribute

    def change_attribute(self):
        self.sub_attribute = different_sub_attribute
```

*The sub class Sub inherits from the* `__init__` *of the super class Super*
*but can also add its own attribute* `sub_attribute` *and own method* `change_attribute`

A sub class can have several super classes:
`class Sub(Super1, Super2, Super3, ... , SuperN):`

**`super()`** can be used instead of calling super class by its name (here Super):
```python
class Sub(Super):
    def __init__(self, super_attribute, sub_attribute):
        super().__init__(super_attribute)
```

**Note**: when using `Super.`, need `self` in parameters, while using `super().`, no self

***Multilevel inheritance***, `super()` refers to the immediate super

***Overriding***: change implementation of method inherited by super
___
##### **Static method**: method with no access to other elements in the class

Ex:
```python
class Calculator:
	"""
	Class that contains methods to perform basic operations.
	"""
	
	@staticmethod
	def multiply(number_one, number_two):
		result = number_one * number_two
		print(f"Muliply: {result}")
		
	@staticmethod
	def add(number_one, number_two):
	result = number_one + number_two
	print(f"Addition: {result}")

calculate = Calculator
sum_result = staticmethod(calculate.add(19,25))
```

**`@staticmethod`** is called "decorator" and is **mandatory**, prevents errors and unexpected behavior
*however*
`staticmethod()`is not mandatory: `calculate.add()` is perfect

Static method classes are just used as *folders* of functions, to organize code, nothing else