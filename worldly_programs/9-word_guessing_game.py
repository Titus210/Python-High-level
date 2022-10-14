#!/usr/bin/python3
"""Guess player that user guess a word if its among the list"""
import random

def get_word():
    """Returns a random great player"""
    players = ["Messi","Ronaldo","Maradona", "Pele","Ribery","Robben","Ronney","Henry","Timothy"]
    return random.choice(players).upper()

def check(player, guesses):
    """checks if letter exist in players.
    Creates and returns string representation of word
    Parameter:
            player:Name of player that is unonimusly created
            guessed: The guessed letter
    Return: Status of words in player name guessed.
    """
    status = ''
    last_guess = guesses[-1]
    matches = 0     # Number of occurences of last guess in word

    #   Loop to check if each letter is in guessed
    for letter in player:
        status += letter if letter in guesses else '*'
        if letter ==  last_guess:
            matches += 1

    if matches > 1:
        print(f'The word has {matches} {last_guess}\'s')
    elif matches == 1:
        print(f'The word has one {last_guess}')
    else:
        print(f"Sorry The player has no {last_guess}'s")
    return status

def main():
    player = get_word() # gets random player
    num = len(player)   # number of letter in random players
    guesses = []        # List  of guess made
    guessed = False

    print(f"The word has {num} letters")

    while not guessed:
        guess = input(f"Guess a player or {num}-letter player name: ")
        guess = guess.upper()

        if guess in guesses:
            print(f"You have already guessed {guess}")
        elif len(guess) == num:
            guesses.append(guess)
            if  guess == player:
                guess = True
            else:
                print('Sorry, that is incorrect')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(player, guesses)
            if result == word:
                guessed == True
            else:
                print(result)
        else:
            print("Invalid Entry")
    print(f'{player} is it! It took you {len(guesses)} tries')
main()







