#!/usr/bin/python3
def read_entire(txt):
	"""
	writes and reads data in binary form
		Parameters:
			txt (char): text to be written in file
	"""
	with open("readFile.txt","w+", encoding = "utf-8") as f:
		print(f'{txt}')
		f.write(txt)
		position = f.tell()
		print(f'Curren position is {position}')
		f.seek(0)
		position = f.tell()
		print(f'Reseted position is {position}')
		reading = f.read()
		print(f'The text is \n {reading}')
tetx = "This is just a random text to show how reading can be done in python to write iin a file called readFile"
read_entire(tetx)
