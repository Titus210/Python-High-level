import re
import sys


def main():
    """Asks user type of operation.    
    """
    print("1. Read From a file...\n2. Write to a file...")
    option = int(input("Please Choose file opration to perform: "))
    if option == 1:
        while True:
            fileName = input(
                "Enter name Of file to read from in format(Filename.txt): ")
            fileFormat = re.search(r'.txt$', fileName)
            try:
                fileFormat.group()
                with open(fileName, 'r') as f:
                    for count, line in enumerate(f):
                        count + 1
                    print(
                        f"File '{fileName}' read successfully, {count+1} lines")
                break
            except FileNotFoundError:
                sys.exit(
                    f"Error while processing file '{fileName}', stopping.")

    elif option == 2:
        while True:
            fileName = input(
            "Enter name Of file to Write from in format(Filename.txt): ")
            fileFormat = re.search(r'.txt$', fileName)
            value = input("Enter Value to write: ")

            try:
                if fileFormat.group():
                    print(f'{fileName} is in correct format')
                with open(fileName, 'a+') as f:
                    f.writelines(value)
                    print(
                        f"File '{fileName}' was successfully written")
                break
            except FileNotFoundError:
                sys.exit(
                    f"Error while processing file '{fileName}', stopping.")


main()
