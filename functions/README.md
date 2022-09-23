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

