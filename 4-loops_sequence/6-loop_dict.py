#!/usr/bin/python3
grades = {'Math':80,'English':70, 'Kiswahili':90}

## Loop through dictonary
print('Looping through a dictonary')
for subj in grades:
    print(f'{subj} \n')

for course in grades.keys():
    print(course)

## Loop through values
print('Loop through Values')
for grade in grades.values():
    print(grade)

## Loop items in dict
for course, grade in grades.items():
    print(f'{course}: {grade}')

