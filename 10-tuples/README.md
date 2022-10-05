##	Tupples
Tupples are like list but unlike list they are `immutable` hence values cant be changed.<br/>
####	Creating
```
	myTuple = (1,"Titus","Men",3434)
```
Passing tupples to a function we need to use parenthesis
```
	def myFunc((myTuple)):
```
another method is using `*args`
```
	def myFunc(*myTuple):
```
One value tuple:
When we dont include a comma after it, its type becomes a string
```
	myTuple = ("Titus",)
```
### Application of tuples
Tuples are used when we want to hold data that wount change in the course of the program.
Example:
-	Longitudes and latitudes
-	Width and height of a section
-	color value i.e rgba e.t.c

