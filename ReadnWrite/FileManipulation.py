import re
import sys


def main():
    """Read and Write text to a given file.
     
    """
    
    text = []
    while True:
        fileName = input(
            "Enter name Of file to read from in format(Filename.txt): ")
        fileFormat = re.search(r'.txt$', fileName)
        try:
            fileFormat.group()
            with open(fileName, 'r') as f:
                for count, line in enumerate(f):
                    count + 1
                    text.append(line.strip())
                print(
                    f"File '{fileName}' read successfully, {count+1} lines")
            break
        except FileNotFoundError:
            sys.exit(
                f"Error while processing file '{fileName}', stopping.")

    while True:
        fileName = input(
            "Enter name Of file to Write from in format(Filename.txt): ")
        fileFormat = re.search(r'.txt$', fileName)
        try:
            if fileFormat.group():
                print(f'{fileName} is in correct format')
            with open(fileName, 'a+') as f:
                f.seek(0, 2)
                f.write("\n")
                for line in text:
                    f.write(f"{int(line)}\n")
                print(
                    f"File '{fileName}' was successfully written")
            break
        except FileNotFoundError:
            sys.exit(
                f"Error while processing file '{fileName}', stopping.")


main()
