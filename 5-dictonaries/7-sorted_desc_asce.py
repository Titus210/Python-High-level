#!/usr/bin/python3
import operator
def sort_value():
	items = {
		 "floor": 100.00,
		 "olive oil": 200.00,
		 "salt": 20.00,
		 "toothpaste": 120.00,
		 "toothbrush": 70.00,
		 "coffee": 180.00
	}
	print(f'Items before sorting:\n {items}')
	sort_descending = sorted(items.items(), key= operator.itemgetter(1), reverse = True)
	sort_ascending = sorted(items.items(), key= operator.itemgetter(1))
	print(f'Items after sorting\n ascending :\n {dict(sort_ascending)} \n Descending: \n {dict(sort_descending)} ')
sort_value()
