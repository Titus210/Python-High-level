# FILE RENAMING
This python script is designed to rename files in a specific directory.<br/>
## History of the Project
After being given my Semester Units I realized they were renamed in a bad format, which was not easy to follow along due to its 
way of organization in the computer<br/>
I decided to change the name format and name precedence to ease access and control over the pdf files.
### File Format Before 
![File Format Before Renaming](https://github.com/Titus210/Python-High-level/blob/master/100%2B_python_Projects/File_Rename/Original.JPG)
## Approach Towards Renaming the documents
The script uses the os and `os.path` modules to navigate the file system 
and perform the renaming operations. <br/>
It also provides options for handling errors and conflicts that may arise during the renaming process.

## Step-by-step Algorithm
1. import the `os` modulel to navigate the file system.
```
    import os
```
2. Create a function where we will execute all our operations
```
    def rename():
        # Code will come here
```
3. Get current working directory tht contains the pdf file using `os.chdir()` and print the __working directory__ using `os.getcwd()` functions in `os` module.
```
    # Get file directory that contains Pdf file 
    try:
        file_directory = os.chdir('C:/Users/Titus/Desktop/LectureNotes')
    except FileNotFoundError:
        print("The directory you specified does not exist.")
        return
    except Exception as e:
        print("An error occurred:", e)
        return
    
    # print current working directory
    current_directory = os.getcwd()
    print(current_directory)
```
__Output:__ <br/>
`C:/Users/Titus/Desktop/LectureNotes`
We have to print the file directory to ensure we are working with the correct folder <br/>
Using handling error approach ensures that we do not fall into errors while working with our directory <br/>

4. Using `for` lop we iterate over all the files using `os.listdir` in the directory and split them into two parts using `os.path.splitext()`:
- the first part is the pdf name
- the second part is the pdf extension
```
    # Loop Through All files in directory
    for file in os.listdir():     
        # split the file extension ".pdf"
        pdf_name, pdf_ext = os.path.splitext(file)
        print(pdf_name)
        print(pdf_ext)
```
The above code returns a tuple with two parts

5.  We then split he files whenever we encounter an hyphen and strip the white spaces around it
```
    # split the file_extension on hyphen
        try:
            unit_name, unit_title, pdf_num, = pdf_name.split('-')
        except ValueError:
            print(f"File {file} does not have the expected format.")
            continue
    unit_name = unit_name.strip()
    unit_title = unit_title.strip()

```
6. For the pdf number which to my preference which i will only need the number and fill it with `0's`
```
    # strip number sign #, and make it 2 digit number
    pdf_num = pdf_num.strip()[1:].zfill(2)
```
7. For the final part we have to arrange the file in the format pdf number, unit name
```
    # Arrange files
    new_name = f'{pdf_num}-{unit_name}{pdf_ext}'
```

8. Using `os.rename()`  function we rename the file from the original to new name
```
        try:
            os.rename(file, new_name)
        except FileExistsError:
            print(f"File {new_name} already exists.")
        except Exception as e:
            print(f"An error occurred while renaming {file}:", e)
```
The Full code example is found below <br/>
[Full Code Implementation](https://github.com/Titus210/Python-High-level/blob/master/100%2B_python_Projects/File_Rename/fileRename.py)

# Time Complexity
The time complexity of the above code depends on the number of files in the directory and the amount of processing done on each file. <br/>
The outermost loop that iterates through all files in the directory using the `os.listdir()` function has a time complexity of` O(n)`, where `n` is the number of files in the directory. <br/>
The `os.path.splitext(file)` function and the `pdf_name.split('-')` function both have a time complexity of` O(m)`, where` m` is the length of the file name. <br/>
The `unit_name.strip(`), `unit_title.strip()`, `pdf_num.strip()[1:].zfill(2)` all have a time complexity of `O(n)`, where` n` is the length of the string.
Finally, the `os.rename(file, new_name)` function has a time complexity of `O(1)` <br/>
Overall, the time complexity of the above code is `O(n*m)`, where n is the number of files in the directory and `m` is the average length of file names.
## File  After 
![File Format After Renaming](https://github.com/Titus210/Python-High-level/blob/master/100%2B_python_Projects/File_Rename/New%20File.JPG)
## Conclusion
This script can be very useful for organizing and maintaining large numbers of files <br/>
This code was written and documented  by [Titus Kiplagat](https://www.linkedin.com/in/titus-kiplagat-5146ba210/)




