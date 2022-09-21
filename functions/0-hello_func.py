#!/usr/bin/python3
"""
	Creating dunction to print name
"""
def say_hello(name):
	print('Hello {}!'.format(name))
name = str(input("Please enter your name"))
say_hello(name)
