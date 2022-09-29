#!/usr/bin/python3
number = 1729
n = int(number ** (1/2))
results = {}
for a in range(n+1):
	for b in range(a):
		result = a**2 + a*b + b**2
		if result in results:
			results[result].append((a,b))
		else:
			results[result] = [(a,b)]
		if result > number:
		 	break
	for x in results:
		if len(results[x]) > 3:
		 	print(x,results[x])
