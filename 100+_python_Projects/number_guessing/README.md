##  Number Guessing Game
This is a popular programmers game that user is prompted to enter a number and 
its range is checked from the answer. <br/>
### How the game works
The user selects a range of numbers where he/ she wants his guess number to situate. 
Each number range has its equivalent number pf trials to guess. <br/>
The table below shows trials per each range

 | range  | no. of trials |
 | ------ | ------------- |
 | 1-10   | 2             |
 | 1- 20  | 3             |
 | 1 - 50 | 4             |
 | 1-80   | 5             |
 | 1- 100 | 6             |
 ###  Code Implementation
 The code is implemented with:
-       Control structures
-       Loops
-       random module

## Modules used.
1. __python-tabulate:__ <br/>
This is a python library to create table to learn more read on [python-tabulate](https://pypi.org/project/tabulate/) <br/>
   `pip install tabulate`

2. __random:__ <br>
3. This is a python library to randomize and create random number feom a given range
   
## Functions
1. __game_range():__ <br/>
This is the main function that runs the game. It displays table of choices on the range and choices. <br/>
Creates an executable control statement that initializes the range and trials per range. <br/>
The function calls __main_game__ function.
2. __main_game()__ <br/>
The playe enters the number to guess and code is run within the range chosen. <br/>
Its also receives arguments from game_range function. <br/>
Using while loop the code is evaluated in steps until the function returns break upon failed execution. <br/>

# Conclusion
This was just a fun game where i was trying to change the way we do guess number game. 
This is an open source project open for code modification, typos rectifications. <br/>

This project was originally developed by [Titus Kiplagat](https://www.linkedin.com/in/titus-kiplagat-5146ba210/)