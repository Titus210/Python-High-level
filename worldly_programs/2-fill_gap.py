#!/usr/bin/python3
def fill_gap(verb, noun,adjective):
	"""
	Fills the users input  to spaces below
	returns story
	"""
	story = "After reading The Alchemst by Paulo Coelho i  {0} that in life every step you is a step shorter towards achieving what the world has in store for you. We live thinking that {1} is just a place where we can live unnintenionally, but from the view of outter picture we fail to live most of lives {2}.".format(verb,noun,adjective)
	return story

def word_input():
	"""Prompts user to enter verb noun and adjective
	passes arguments to fill_gap parameters"""
	noun = str(input("Enter a noun"))
	verb = str(input("Enter a verb"))
	adjective = str(input("Enter an adjective"))
	# calling fill function
	filled = fill_gap(verb,noun,adjective)
	print("Here is yout beautifull story")
	print(filled)
word_input()
