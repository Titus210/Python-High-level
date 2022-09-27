#!/usr/bin/python3
# appending user input in place of 20000
numbers = [2,200,[4000,[10000,20000],200],10000]
print(f'Numbers before appending is: \n {numbers}')
inputted =input("Which number do you want to insert")
numbers[2][1][1].append(20000)
print(f'Numbers after appending is :\n {numbers}')
