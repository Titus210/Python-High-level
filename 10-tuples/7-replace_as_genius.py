#!/usr/bin/python3
myTuple=  [(12, 34, 44), (12, 22, 49), (12, 100, 200)]
print([i[:-1] + (100,) for i in myTuple])
