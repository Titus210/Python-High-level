#!/usr/bin/python3
""" Grade input and calculate users averahe on subjects per grade"""

def main(grades):
	"""User grade input"""
	subjects = ["Maths","English","French","Geography","History"]
	for subject in subjects:
		marks = int(input(f"Enter your grade in {subject}: "))
		grades[subject] = marks
		print(f'Your grade in {subject} is {marks}')
	return grades

grades = {}
main(grades)

def averages(grades):
	total = 0
	for value in grades.values():
		total += value
	items = len(grades.values())
	average = (total/items)
	print(f'Your average in {items} subjects is {average}')

print(grades)
print(averages(grades))
