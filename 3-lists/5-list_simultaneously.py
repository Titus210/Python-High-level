#!/usr/bin/python3
list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]
for x, y in zip(list1,list2[::-1]):
	print(x,y)
