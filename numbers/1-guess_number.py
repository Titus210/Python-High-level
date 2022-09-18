#!/usr/bin/python3
import random

def guess_number():
	answer = random.randint(0,100)
	while True:
		user_num = int(input("What is your guessed number between 0 and 100?"))
		if user_num == answer:
			print(f'Genius! You\'ve correctly guessed {user_num} as the number.')
			break
		if user_num < answer:
			print(f'Your guess of {user_num} is low! Try again')
		else:
			print(f'Your guess of {user_num} is high! Try again')
guess_number()
