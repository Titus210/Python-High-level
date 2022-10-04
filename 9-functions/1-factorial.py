#!/usr/bin/python3
def factorial(num):
	"""This is a function to find factorial
	of  number inserted by user"""

	# base case
	if num == 1:
		return 1
	else:
		return (num * (num -1))
number = int(input("Please enter number you want to insert"))
print(f'The factorial of {number} is {factorial(number)}')

