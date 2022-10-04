#!/usr/bin/python3
"""sum numbers from 0 to 100"""
def  sum_numbers():
	"""
		Methods:
			range(): give number from 0:100
	"""
	n = 100
	numbers = []
	for num in range(1,n+1):
		numbers.append(num)
	print(numbers)

	def print_sum(numb):
		"""Printing sum in each index
			Parameters:
				num: list of numbers from 0 to 100
		"""
		summ = 0
		for i in numb:
			summ += i
			print(f"The sum in from number {i-1} to {i} is {summ}")
		print(summ)
	print_sum(numbers)
sum_numbers()




















