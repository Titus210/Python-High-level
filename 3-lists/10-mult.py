#!/usr/bin/python3
def mult_ply(lisst):
	lists = 1
	for i in lisst:
		lists = lists * i
	return lists
result = [1,2,3,4,5,6,7,8,9,10]
print("The product of elements in a list is {}:".format(mult_ply(result)))
