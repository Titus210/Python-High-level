#!/usr/bin/python3
"""
	How many pizza needed:
		input:
			number of people
			number of slices per pie
			number of slices each person will eat
		output:
			number of pizza needed
"""
people = int(input("Enter number of people: "))
slices_person = int(input("How many slices will each person eat: ")) # typo error
slices = int(input("Enter slices in each pie: "))
def slices_needed(people,slices,pie):
	pizza = people * slices
	no_needed = pizza / pie
	print(f"The number of pizza needed is {no_needed}")

slices_needed(people,slices_person,slices)
