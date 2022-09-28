## 		Files
***
###	Introduction
**Important terms**<br/>
-	File management: This is manipulation of data in a file.
-	File: This is a resourse foor recording data discretely in a computer storage device.
There are vatious ways of handling a file:<br/>
1.	Opening.
2.	Perform action i.e read or write
3.	Closing.
Python has the ability to perform all these file operations using methods and keywords.<br/>
Files have the ability to store data  and save files even if the volatile (Random access memory) is turned off
####	Opening a file
we use build-in function `open()` function to open a file, which returns a file object called handle.<br/>
**Modes in opening a file**
-	`a`:(append) - opens a file for appending at the end of the file without truncating end of the file without truncating.
-	`w`:(write) - Opens a file for writting and creates a new file if it doesnt exist else it rewrites existing one.
-	`r`:(read) - Opens a file for reading its default in `open()` function.
-	`x`:(exclusive) - Opens files for exclusive creation. If  file exists operation fails.
-	`t`:(text) - Opens file in text mode(default).
-	`b`:(binary) - OPens file in binary form.
-	`+`(updating): Opens files for updating( reading and writtin)

`open()` attribute takes three arguments:
```
	f = (filename,mode,unicode="uft-18")
```
**Character encoding**: encoding attribute specifies string encoding and using `uft-18` is appropriate else the computer will take default that is available in the local storage since its platfotm dependent.
```
	import locale
	locale.getprefferedencoding()
```
###	Reading files
We open file using `r` in reading mode.
-	`read(size)` to read the size of data . If size is not specified it reads until the end of line.
-	`seek(position)` changes position of cursor.
-	`tell()` returns current position
-	`readline` reads individual lines of file until where there is a new line
-	`readlines` returns list of remaining lines of entire file

```
	with open("read.txt,"w",encoding = "uft-8") as f
	f.write("First code in file")
	f.write("second code in file")
	f.write("last code in file")
	f.read(4)	# reads first 4 data
	f.tell()	# tels file position
	f.seek(1)	# moves cursor to position 1
```
We can use for loop to iterate though a file
```
	for line in f:
		print(line, end = "")
```
###	Closing files
When done with operation we need to close files. We can close file with various methods
-	`close` method

```
	f.close
```
-	`try ...finally` block
THis method closes file if error is encounntered
```
	try:
		f = open("try.txt", "w", encoding = "uft-8")
	finally:
		f.close
```
-	`with` statement
This ensures file is closed when code is exited from block
```
	with open("with.txt", encoding = "uft-8") as f:
		# code inside
```

