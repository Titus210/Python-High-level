# import modules
import random
from tabulate import tabulate

welcome_msg = "\t\t \
   \n Welcome to the guessing game.\n\n \
    \t Game RULES: \n \
1. You have specific trials to guess depending on the range you \n choose from range table below \n"
print(f"{welcome_msg.center(30, ' ')}")


def game_range():
    data = [["1-10",  2],
            ["1-20",  3],
            ["1-50",  4],
            ["1-80",  5],
            ["1-100", 6]
            ]
# define header names
    col_names = ["range", "no. of trials"]
    print(tabulate(data, headers=col_names))

# ask user for range
    no_range = int(input("Please enter a range: 0,1,2,3,4"))
    range = None
    trials = None
    if no_range == 0:
        range = 10
        trials = 2
        main_game(range, trials)
    elif no_range == 1:
        range = 20
        trials = 3
        main_game(range, trials)
    elif no_range == 2:
        range = 50
        trials = 4
        main_game(range, trials)
    elif no_range == 3:
        range = 80
        trials = 5
        main_game(range, trials)
    elif no_range == 4:
        range = 100
        trials = 6
        main_game(range, trials)
    else:
        no_range = int(input("Please enter a range: 0,1,2,3,4: "))


def main_game(range, trials):
    """Player enters number to guess if answer is correct he wins else loses if trials deplete

    Args:
        range (integer): this is the range of number user wants to guess
        trials (integer): this is the number of trials per range decremented
    """


#  generate answer from range
    answer = random.randint(0, range+1)
    while True:
        
        if trials == 0:
            print("You have no more chances remaining")
            break

        else:
            try:
                user_guess = int(input("What is your guess: "))
            except ValueError:
                print(f"{user_guess} is not integer")

            if user_guess == answer:
                print(f'Congratulations! {user_guess} is a correct guess')
                break
            elif user_guess > answer:
                print(
                    f'{user_guess} is high! You have {(trials -1)} chance(s) remaining')
            elif user_guess < answer:
                print(
                    f'{user_guess} is low! You have {(trials -1)} chance(s) remaining')

        trials = trials - 1

game_range()

