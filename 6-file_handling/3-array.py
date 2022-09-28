#!/usr/bin/python3
def file_array(fName):
	"""
	store file in an array
	args:
		text to append in array
	"""
	content_array = []
	with open("array.txt","w", encoding='utf-8') as f:
		f.write(fName)
	with open("array.txt",encoding='utf-8') as f:
		for line in f:
			content_array.append(line)
		print(content_array)
text = "This is just a random text with some initial fdkfjd reoek djksdk"
file_array(text)
