#!/usr/bin/python3
num = {34, 12, 54, 23, 21, 74, 34, 11}
def prime_number(number):
	condition = 0
	iteration = 2
	while iteration <= number / 2:
		if number % iteration == 0:
			condition = 1
		break
			iteration = iteration++
	if condition == 0:
		print(f"{number} is a prime number")
	else:
		print(f"{number} is a not a prime number")
	for i in num
		prime_number(i)
