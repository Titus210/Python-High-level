#		Functions
***
**Rule number one**: Don't repeat yourself(DRY). <br/>
###	Introduction
Functions are code block that can be used several times. It helps you to write a code in modules which can be used repeatedly in a program to avoid repetition of code. <br/>
**Importance** <br/>
1. Helps to reuse the code on different parts of program.
2. Saves time.
3. Easy to debug a program.
###	Implementation
We use def keyword to define a function
```
	def funtion_name(parameter):
	# code to execute
```
Function calling
```
	function_name(argument)
```
We can also use default parameter
```
	def hello_name(name = 'user'):
		print('Hello {}!'.format(name))
	name = input("Please enter your name")
	hello_name(name)
```
###	More and rules
When a function accepts parameters they can also be called positional parameters, because order is important.
```
	def cat_name(first,last):
		print('Hello {} and {}'.format(first,last))
	cat_name(first = 'Shazzy', last = 'fineey')	# Hello shazzy and finney
	cat_name(last = 'bazyy', first = ' milley')	# Hello milley and shazzy
```
We can also combine required and optional parameters
```
	def say_hello(first, last = "User"):
		print('HEllo {}! {}!'.format(first,last))
	fname = input("Please enter your first name)
	sname = input("Please enter second name")
	say_hello(fname)
	say_hello(fname,sname)
```
Python provides arbitary arguments which allows us to to specify no of arguments when we dont kow total arguments that should be passed in the function
```
	def user_names(*names):
		"""This function greets 
		everyone in the tupple"""
		for name in names:
			print("Hello {}!".format(name))
	greet("Ashley,"Titus","Lizzy","halsey")
```
###	Using docstrings
First statement of function is  a documentation string, or docstring in short
We can create docstrings by sorrounding text with three double quotes. Its always a brief summary of the function.
```
	def say_hello(name):
		"""Say Hello."""
		print('Hello {} {}!'.format(name)
	help(say_hello)
```
`help()` function helps to acces the docstring by passing name of function needed to be accesed.
'docstring' are available  as `__doc__` function
###	return statement
They are used to return data using `return` statementThis makes it possible to return data we need
```
	def odd_even(number):
		"""Determine if number is odd or even"""
		if number % 2 ==0:
			return 'Even'
		else
			return 'Odd'
	number = input("Please enter an integer number:")
	result = odd_even(number)
	print(result)
```
## Recursion
This is a function that calls itself. Example placing mirror in parrarel form adjusted	
```
		def recurse():
			recurse()
		recurse()
```
**Advantages of recursion**
-	Makes code look clean and elegant
-	complex task can be frocen to sub-programs
-	Sequential generation is easier than nested iteration
**Disadvantages of recursion**
-	Logic soometimes is hard to follow
-	Expensive, insufficent and take large memory
-	Hard to debug


## Lambda(Anonymus) Functions
This is a function without a name it is defined with `lambda` keyword
```
	lambda arguments : expression
```
They are created whenever function objects are required It can take multiple arguments but has only one expression.
```
	mult  = lambda x: x * 2:
	print(mult(7))
```
Usefull when we require a nameless function for short period of time. We use it as argument to a higher order function function that can take in other functin as arguments.<br/>
Used with `filter()` , `map` and other in-build functions
1.	Using with filter() <br/>
`filter()` takes function and list of arguments. It returns true for elements true in the list.
```
	# users in the podium
	users = [1,12,13,14,12,30,1,22,34,14,12,12]
	less_10 = list(filter(lambda x: (x < 10), users))
	print(less_10)
```
2.	Using map() <br/>
Takes function and list of arguments. New list is returned containing each element in list with returned function in each
```
	grades = [10,4,3,6,7,3,8]
	doulbe_grade = list(map(lambda x * 1.5, grades))
	print(double_grade)
```
##	Global, local and nonlocal
When we write a variable inside a function its `local` by default, a variable outside a function is global by default.
```
	x = "Hello"	# global
	def say_name(name):
		greet = "{} {} Its  on sunday".format(x,name)	# Local
		print(greet)
```
1. Global <br/>
`global` keyword allows us to modify variablea outside current scope.
```
	x = "Hello"
	def say_hello(name):
		global x
		x = "Jambo"
```
We can create a file holding global variables that can be shared across modules <br/>
```
	greet = "Hello"
	 date = "sunday"
````
save file as `hello.py`
```
	import hell

	 hello.greet
	 hello.date
```
2.  Nonlocal variables are used in nested function where scope is not defined hence it can neither be local nor global scope. We use `nonlocal` keyword to define. <br/>
Changes in lonlocal affects local variable
```
	 def outer():
		 x = "Local to outer"
		 def inner():
			 nonlocal x
			 x = "nonlocal"
		inner()
		print(inner()) # nonlocal
	print(outer())	# nonlocal
```
