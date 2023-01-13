#!/usr/bin/python3
""" Ask user to enter two string of numbers \
Print sum of floating point"""

def print_sum(x,y):
    """Printing sum of two integers
        Args: 
            x, y(integer): Value of float
    """
    sum = float(x + y)
    print(f"The sum of {x} and {y} is {sum}")

def main():
    """Asks user to enter value of two inegers"""
    try:
        num_1 = float(input("Please Enter first float number: "))
        num_2 = float(input("Please Enter second floating number: "))
    except ValueError:
        print("Enter A valid Decimal Number")
        main()
    print_sum(num_1, num_2)

main()
