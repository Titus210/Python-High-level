#!/usr/bin/python3

import random
import time
"""Calculates Time Delta to add random numbers to a list using different operations"""

def concenate_Strings(iterations):
    """ Using sring concatenation"""
    start_time = time.perf_counter()
    numbers = ''
    for i in range(iterations):
        num = random.randint(1,100)
        numbers += ',' + str(num)
    end_time = time.perf_counter()
    time_delta = end_time - start_time
    print(f"Concatenate Strings: {time_delta}")

def listAppend(iterations):
    start_time = time.perf_counter()
    numbers = []
    for i in range(iterations):
        num = random.randint(1,100)
        numbers.append(str(num))
    numbers = ", ".join(numbers)
    end_time = time.perf_counter()
    time_delta2 = end_time - start_time
    print(f"List Appending: {time_delta2}")

def listComprehension(iterations):
    start_time = time.perf_counter()
    numbers = str(random.randomint(1,100) for i in range(1,iterations +1))
    numbers = ", ".join(numbers)
    end_time = time.perf_counter()
    time_delta3 = end_time - start_time
    print(f"List Comprehension: {time_delta3}")


def main():
    iterations = int(input("Please Enter Number of Iterations"))
    print("\n The Time deltas are as follows")
    listComprehension(iterations)
    listAppend(iterations)
    concenate_Strings(iterations)

main()




