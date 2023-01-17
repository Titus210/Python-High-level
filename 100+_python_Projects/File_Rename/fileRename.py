import os
# Navigate file system


def rename():
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

    # Loop Through All files in directory
    for file in os.listdir():

        # split the file extension ".pdf"
        pdf_name, pdf_ext = os.path.splitext(file)

        # split the file_extension on hyphen
        try:
            unit_name, unit_title, pdf_num, = pdf_name.split('-')
        except ValueError:
            print(f"File {file} does not have the expected format.")
            continue

        unit_name = unit_name.strip()
        unit_title = unit_title.strip()

        # strip number sign #, and make it 2 digit number
        pdf_num = pdf_num.strip()[1:].zfill(2)

        # Arrange files
        new_name = f'{pdf_num}-{unit_name}{pdf_ext}'

        # rename file
        try:
            os.rename(file, new_name)
        except FileExistsError:
            print(f"File {new_name} already exists.")
        except Exception as e:
            print(f"An error occurred while renaming {file}:", e)

rename()
