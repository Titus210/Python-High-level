#!/usr/bin/python3
"""
	Removes a random person from the list to make fair decision on people going for trip
"""
import random

def random_person(persons):
	choise = random.choice(persons)
	persons.remove(choise)
	return choise


def main():
	people = ["Titus","Kevin","sylvia","Antony", "Moses","Julie"]
	removed_person = random_person(people)
	print(f'Sorry {removed_person} you could not make for the trip')
	print(f'The remaining people are {people}')

main()

