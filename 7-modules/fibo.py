#!/usr/bin/python3
def fib(n):
	"""Writes fibinacci series upto n
	Parameters:
		n: LAst fibonacci number
	"""
	a ,b = 0, 1
	while a < n:
		print(a, end = " ")
		a, b = b , a+b
	print()

def fib2(n):
	"""
	Returns:
		Fibonacci series upto n
	"""
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
	a, b = b , a+b
	return result

