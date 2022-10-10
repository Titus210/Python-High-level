#!/usr/bin/python3
"""Checks if user is eligible  for voting and drinking"""
def eligibility(name,age):
    if age >= 21:
        print(f'{name}, you can vote and drink.')
    elif age >= 18:
        print(f'{name}, you can vote but can\'t drink.')
    else:
        print(f"Sorry {name}, youre an underage, you can\'t vote nor drink")

name = input("Please Enter your name ")
age = int(input("Please Enter your age "))
eligibility(name,age)
