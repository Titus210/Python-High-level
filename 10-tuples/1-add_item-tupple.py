#!/usr/bin/python3

# create a tuple
myTuple  = (1,"Titus",2022)
print("Elements before inserting")
for i in myTuple:
	print(i)
mylist = list(myTuple)
list1 = [2,"Henry",2023]
mylist.extend(list1)
myTuple = tuple(mylist)
print("Elements after inserting ")
for i in myTuple:
	print(i)
