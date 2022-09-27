#!/usr/bin/python3
num = 4
lists = ["Kiplagat","Python","cat","ls", "dir", "Pychology"]
def list_size(lists):
	num = 5
	j = 0
	for i in lists:
		if len(lists[j]) > num:
			print(f'String {i} is greater than {num}')
		else:
			print(f'String {i} is small than {num}')
		j += 1
list_size(lists)
