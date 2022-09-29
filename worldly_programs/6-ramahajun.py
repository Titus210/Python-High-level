#!/usr/bin/python3
"""smallest number expressible by sum of 2 cubes"""
number = 1729
n = int(number ** (1/3))

cubes = {}
for i in range(n+1):
	for j in range(i):
		result = i **3 + j **3
		if result in cubes:
			cubes[result].append((i,j))
		else:
			cubes[result] = [(i,j)]
		if result > number:
		 	break
	for x in cubes:
		if len(cubes[x]) > 1:
				print(x, cubes[x])
