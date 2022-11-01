#!/usr/bin/python3
"""Catch an error for dividing by zero"""
def divide_zero(num):
    """divides number by zero
        Args:
            num: THis is number enterd by user to be divided
        Return:
            error if it occurs or not
    """
    try:
        num/0
    except:
        print("You cannot divide number by Zero")

num = int(input("Please Enter a number"))
divide_zero(num)
