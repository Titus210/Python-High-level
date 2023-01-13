#!/usr/bin/python3
""" Validate date in python """

import time

def validate_Birthday():
    Result = None
    while True:
        bDay = input("Please Enter you BirthDay in format: dd/mm/yyyy")
        try:
            date = time.strptime(bDay, "%d/%m/%Y")
            print(f"Your Birthday is: {bDay}")
            result = True;
            break
        except ValueError:
            print(f"Sorry!, {bDay} is invalid date!")
            result = False
            continue
validate_Birthday()


