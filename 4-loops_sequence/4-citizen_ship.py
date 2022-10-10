#!/usr/bin/python3
""" Check if user is a citizen"""
name = input("Please enter your name ")
citizen = input("Are you a citizen? \n Reply:\n Y if yes \n N if no: \n").lower()
is_citizen = "Sorry you cant apply for National Identity" if citizen == 'n' else "Apply for Identity card"
print(f"{name}" + is_citizen)
