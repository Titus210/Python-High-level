#!/usr/bin/python3
import read_entire

def read_n_lines(txt,num):
	"""
	writes and read file to a specified number in the text
		Parameters:
			txt(char): Text to be written and read
			num(int) : Number to which reading stops
		Returns:
			nothing
	"""
	with open("nlines.txt","w",encoding = "utf-8") as f:
		f.write(txt)
		f.seek(0)
		reading = f.read(num)
		print(f'The text to {num} position is {reading}')
position = int(input("Enter Position between 5-40 where you want to insert"))
while position > 50 or position < 5:
	position = int(input("Enter correct format between 5 and 40"))
text = read_entire.tetx
read_n_lines(text, position)
