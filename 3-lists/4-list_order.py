#!/usr/bin/python3
name = input("Enter your name")
list1 = ["Hello","Good"]
list2 = [f'{name}','Morning']
conc =  [ i + j for i in list1 for j in list2]
print(conc, end = " ")
