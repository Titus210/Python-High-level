#!/usr/bin/python3
"""Replace last item of tuple in a list"""
myList = [(12,34,44),(12,22,49),(12,100,200)]
print(f'my List before changing is {myList}')
## selecting tuple at index 2 of list
myTuple = myList[2]
## making list to a tuple
new_list = list(myTuple)
## change new list item 200 to 1000
new_list[2] = 1000
### returning to original
new_myTuple = tuple(new_list)
myList.insert(2,new_myTuple)
myList.pop(3)
print(f'My list after changing is {myList}')
