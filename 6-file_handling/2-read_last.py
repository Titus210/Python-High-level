#!/usr/bin/python3
import sys
import os
def read_from_end(fName, lines):
	"""
	args:
		fName : file name.
		lines : number of lines
	check file size using os
	list to hold items
	"""
	bsize = 8192
	fsize = os.stat(fName).st_size
	iter = 0
	with open(fName) as f:
		if bfsize > fsize:
			bsize = fsize-1
			date = []
			while True:
				iter += 1
				f.seek(fsize-bsize*iter)
				data.extend(f.readlines())
				if len(data) >= lines or f.tell() == 0:
					print(''.join(data[-lines:]))
					break

nlines = open("nlines.txt","r")
read_from_end(nlines,2)
