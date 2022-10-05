#!/usr/bin/python3

# creating tuple
items = ("Green","Cabbage","nike","safaricom",2022)

#unpacking
	# Number of variables must equal the number of items in tuple
color,vegetable,label,internet,year = items

print(f'I will wear {color} and eat a {vegetable} though i must not wear a {label} shoe \
		however i must not forget my update my {internet} simcard by october {year}')
