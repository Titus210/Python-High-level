#!/usr/bin/python3
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key = lambda x: float(x[1]), reverse = True))
