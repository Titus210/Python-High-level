#!/usr/bin/python3
import random


def function():
    for x in range(10):
        yield x**2

## Returning generator object
g1 = function()
print(g1)

for x in g1:
    print("Received",x)

arr1 = list(g1) ## Returns arr1 = []  Previous loop consumed all values
print (arr1)

g2 = function()
arr2 = list(g2) ## Returns a list arr2 = [1,2, .... ]
print(arr2)


