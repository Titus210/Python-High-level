#!/usr/bin/python3
"""Implementing else in for and while loop"""
def main():
    """Promts user to enter number.
    for loop:
            Iterates until the number is encountered.
    """
    print("For loop")
    num = int(input("Please enter anumber: "))
    for i in range(5):
        if i == num:
            break
        print(i)
    # For else block
    else:
        print(f"Completed Iteration without reaching {num}")

    #While loop
    i = 0
    num = int(input("Please enter number: "))
    while i <= 5:
        if i == num:
            break
        print(i)
        i += 1
    else:
        print(f"Completed loop without reaching {num}")
main()

