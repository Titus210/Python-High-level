#!/usr/bin/python3
import random
"""user generator to avoid local Variables"""

##  List loop
def get_rand_nums(low = 1, high = 100 , num = 5):
    for numbers in range(num):
        yield random.randint(low,high)

print("First time loop")
numbers = get_rand_nums(1,100,5)
for num in numbers:
    print(num)
print("Second loop")
numbers = get_rand_nums(1,100,5)
for num in numbers:
    print(num)

