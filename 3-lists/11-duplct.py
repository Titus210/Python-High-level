#!/usr/bin/python3
def duplc(lisst):
	lists = lisst
	print(f'List with repeated items :{lists}')
	for i in lists:
		if i in lists:
			lists.remove(i)
	return lists
vers = [1,2,3,43,3,3,3,4,20]
print(f'The list with no repeat : {duplc(vers)}')
