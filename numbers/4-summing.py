#!/usr/bin/python3
def mySum(*numbers):
	output = 0
	for x in numbers:
		output += x
	return output
print (f'The total sum is {mySum(10,10,20,20)}')
