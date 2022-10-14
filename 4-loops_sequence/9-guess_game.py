#!/usr/bin/python3
import random

"""
    guessing game using continue and break
"""

def is_valid(s):
    """Check if number is digit and less than 100"""
    return s.isdigit() and 1 <= int(s) <= 100

def main():
    number = random.randint(1,100)
    guessed_number = False
    guess  = input("Please Enter a guess between 1 and 100: ")
    num_guess  = 0

    while not guessed_number:
        if not is_valid(guess):
            print("I woun't count that.")
            guess = input("Please enter a number between 1 and 100")
            continue    # Skips to next iteration of loop

        num_guess += 1
        guess = int(guess)

        if guess < number:
            guess = input("Too low, Try again: ")

        if guess > number:
            guess = input("Too high, Try again: ")

        else:
            print("Genius!, You've got it right in", num_guess)
            guessed_number = True

    print("Thanks for playing")
main()


