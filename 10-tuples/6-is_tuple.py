#!/usr/bin/python3
num = [1,2,3,4,(22,34,34)]
ctr = 0
for i in num:
	if isinstance (i,tuple):
		break
	ctr += 1
print(f'Tuple is at index {ctr}')
