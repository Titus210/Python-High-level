#!/usr/bin/python3
def small_list(lists):
	minimum = lists[0]
	for i in lists:
		if  i < minimum:
			minimum = i
	return minimum
print("The minimum in list is {}".format(small_list([12,21,34,13,54,32,2])))
