#!/usr/bin/python3
"""Check users  age"""
def is_valid_age(s):
    """True if the eage entered is a digit"""
    return s.isdigit() and 1 <= int(s) <= 113

def main():
    """Checks if users age is a digit.
        calls function is_valid_age()
        return:
                Users eligibility
    """

    name = input("Please Enter your name: ")
    age = input("Please enter your valid age: ")

    while not is_valid_age(age):
        print(f'{name}, Please enter a valid age!')
    age = int(age)
    if age >= 21:
        print(f'{name}, You can drink, but responsibly')
    elif age >= 35:
        print(f'{name}, You can drink but watch out for your health')
    else:
        print(f'{name}. You are very young and its a criminal offense')
main()
