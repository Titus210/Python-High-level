#!/usr/bin/python3
n = int(input("Enter a number"))
dictn = dict()

for i in range( n+ 1):
	dictn[i] = i * i
print(dictn)
