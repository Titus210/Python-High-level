#!/usr/bin/python3
def count_list(*numb):
	"""counts number in list.
	does the sum of list
	returns average of sum"""
	for i in numb:
		no_list =len(numb)
	addition = 0
	for i in numb:
		addition += i
	return addition/no_list

count = count_list(10,20,10,10,20)
print(count)
