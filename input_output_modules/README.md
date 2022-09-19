## Python Input and Output
***
 **python input**
Python has inbuild method thatis used to get input/data from the user <br/> We usw `input([prompt])`. Prompt is used to display message to user. <br/>
The function returns a string type, therefore we need to typecast it to its equivalent data type:<br/>
-	```int(input("Enter age"))  #typecast to integer```
-	```float(input("Enter  amount to spend"))  #typecast to float```
-	```bool(input("Are you willing to pay every amount?")) ## typecast to boolean ```
<br/>
**python output**
Its used to display output to the user. ```print("Hello {user}".format(user = name)) ```
> print(*object, sep=' ', endl = '\n' ,file = sys.stdout, flush = False)
The print parameters are:
-				object: The output shown to user
-				sep: Makes a space by default
-				end: Skips to the next line
-				file: Where to display
**Output Formating**
This is where we format variables to make a human readable output. It is done in several ways
-		Using <i>string modulo opetator `%` <\i> <br/>
	```print("%s your grade is %3.2f "%("Titus",85.74)) ```
-		Using  <i> Format method <\i>
We use `str.format to format strings by adding `{}`.
	```
		name = "Titus Kiplagat"
		print("Hello {} grade is {} ").format("Titus",85.77))
		print('{:<20}'.format(name))	 	# Alligns name to left
		print('{:^20}'.format(name))		# Alligns name to center
		print('{:>20}'.format(name))	 	# Alligns name to right
	```
-	Using <u> string method </u>
This is done using slicing and concatenation operations.
We use `str.center()`, `str.ljust()`, `str.rjust()`
	```
		name = "Titus Kiplagat"
		print(name.center(30,#))	# ######Titus Kiplagat ######
		print(name.ljust(10,-))		# Titus Kiplagat --------
		print(name.rjust(10,-))		# ----------Titus kiplagat
	```
###		Python Module
Modules are files containing python statements and definitions. They end with `.py`
They are used to break down large program to small managable organized files, hence provide reusability.
Important functions can be defined in a module then we use `import` keyword to import. Instead of copying definitions to different programs.<br/>
Creating a module:
	```
		def add(a,b):
			'''This program adds two numbers 
			and returns a result"""
			result = a + b
			return result
	```
Importing module:
We use access definitions inside using  `dot operator`
	```
		import addition
		addition.add(20,10)
	```
Import with renaming:
	```
	   import math as m
	   print("The value of pi is  ", m.pi)		#  math will not be recognized on scope
	```
from...import statement:
	```
	   '''Used to specify module names to import without importing as whole
	   '''
	     from math import pi
	     print("The value of pi is ", pi)
	```
Import all names(definitions)
	```
	   ''' Used to import all names using (*) operator
	     It includes names visible on scope except
	     ones starting with underscore (private)
	     Not good practice hampers readerbility and causes duplication of identifiers
	   '''
	   from math import  *
	   print("Value of pi is ",pi)
	```
Search path:
	```
	   import sys
	    sys.path
	     '''
	     ['',
	     'C:\\Python33\\Lib\\idlelib',
	     'C:\\Windows\\system32\\python33.zip',
	     'C:\\Python33\\DLLs',
	     'C:\\Python33\\lib',
	     'C:\\Python33',
	     'C:\\Python33\\lib\\site-packages']
	     '''
	```
It finds first  the input modules then if not found it looks inside sys.path . We can add and modify our path.
Reloding a module:<br/>
Python imports a module only once. We use `reload()` function to reload a module inside `imp` module
	```
	   import imp
	   import add
	   add(20,10)
	   import reload(add)
	   add(30,50)
	```
dir() function:<br/>
We use `dir` function to find names defined in  modules
	```
		dir(adding)
		['__builtins__',
		'__cached__',
		'__doc__',
		'__file__',
		'__initializing__',
		'__loader__',
		'__name__',
		'__package__',
		'add']
	```
	  Items with underscore i.e  __name__ means they are not user defined
	```
	   import math
	   dir ()
	   ['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']
	```
***
### Conclusion
This document was written by [Titus Kiplagat](https://ke.linkedin.com/in/titus-kiplagat-5146ba210) <br/>
Refferences:
[python documentation](https://docs.python.org/3/tutorial/modules.html)<br/>
[real python](https://realpython.com/python-modules-packages/)
