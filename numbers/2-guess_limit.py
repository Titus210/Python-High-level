#!/usr/bin/python3
import random
def guess_limit():
	answer = random.randint(0,50)
	num  = [1,2,3,4]
	for i in num:
		if i == 4:
			print("You have no more chances remaining")
		else:
			user_num = int(input('What is your guess between 0 and 10?'))
			if user_num == answer:
				print(f'Congratulations! {user_num} is a correct guess')
				break
			if user_num < answer:
				print(f'{user_num} is low! You have {3-i} chance(s) remaining')
			else:
				print(f'{user_num} is high! You have {3-i} chance(s) remaining')
		i += 1
guess_limit()

