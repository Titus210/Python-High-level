#!/usr/bin/python3
import random
def get_random_nums(low,high,num):
    numbers = []
    for number in range(num):
        numbers.append(random.randint(low,high))
    return numbers

numbers = get_random_nums(1,100,5)
print("First Iteration")
for num in numbers:
    print(num)
print("second iteration")
for num in numbers:
    print(num)

