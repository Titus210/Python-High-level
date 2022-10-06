#!/usr/bin/python3
def main(text):
	"""Write a file to check use of split lines"""
	with open("name.txt","w",encoding = "utf-8") as f:
		f.write(text)
text = "Eldoret\n Kiambu\n Nakuru\n Busia\n Nairobi\n Naivasha"
main(text)
