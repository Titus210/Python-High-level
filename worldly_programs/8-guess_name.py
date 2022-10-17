#!/usr/bin/python3
"""
Guess the number: This is a program to ask user to guess a number
	Start:
		import random <-- answer
		Input number
		number greater than answer
			Display: Too high
		number less than answer
			Display: Too low
		number equal to answer
			Display Correct guess
"""
import random
def guess_number():
	"""
			num: number inputed by user
			name: users name
	"""
	name = input("Please Enter your name")
	answer = random.randrange(0,50)
	num = int(input("Enter guess number between 0 and 50"))
	while num != answer:
		if num < answer:
			print("Number is too low")
			number = int(input("Enter the number again "))
		elif num > answer:
			print("Number is too high")
			number = int(input("Enter the number again "))
		else:
			print("{} is a correct guess {}! You're a genius!".format(num,name))

guess_number()


