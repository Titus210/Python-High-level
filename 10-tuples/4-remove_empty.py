#!/usr/bin/python3
"""Remove empty items in tuple"""
myTuple = ((),(""),("Titus",21),(),("Kevin",12),("Ashley",18))
print("Tuple before romoving is {0}".format(myTuple))
# Convert tuple to a list
mylist = list(myTuple)
print(mylist)
for i in mylist:
	if i == ():
		mylist.remove(i)
# convert list to a tuple
myTuple = tuple(mylist)
print("My Tuple after removing is:{} ".format(myTuple))
