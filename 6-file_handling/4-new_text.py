#!/usr/bin/python3
def list_word(lists):
	"""
	Open file and converting list to word
	save file to song
	"""
	with open("list_file.txt","w+",encoding = "utf-8") as f:
		for i in lists:
			f.write("%s\n" %i)
lists = ["Green","Yellow",123,24,47,"VAnilla","Chocolate"]
list_word(lists)
print("List entered is \n ")
with open("list_file.txt",encoding = "utf-8") as f:
	print(f.read())

