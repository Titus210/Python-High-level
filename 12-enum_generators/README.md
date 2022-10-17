#		Generators
***
Generators are  laxy iterators created by genarator functions called `yield` using (an expression `for x in an_iterator`)
Generator expressions are similar to list, dictonaries and set comprehensions but enclosed with parentheses. The parentheses do not have to be present when they are used as sole argument of function call.
```
	expression = (x ** 2  for x in range(10))
```
Generator functions are are similar to regular function, except that theve one more `yield` statement in they in body. Such functions cannot **return** any values , however emppty returns are allowed if yu want to stop the generator arly
```
	def funtion():
		for x in range(10):
			yield x ** 2
```
Calling generator function produces generator object, which can be iterated over. which can be traversed once
### Advantages of generators
-	They are not immediately excecuted hence when called it returns generator object without executing hence saves alot of space
-	Used in Data Science where large amount of data is is used.
***
If you need values of generators more than once we might store yielded values as a list than regenerate them 
