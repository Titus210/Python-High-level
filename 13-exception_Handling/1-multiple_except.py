#!/usr/bin/python3

def divide():
    try:
        numerator = int(input("Enter a numerator"))
        denomenator = int(input("Enter Denomenator"))
        result = numerator / denomenator
        print(f'{numerator} divided by {denomenator} equals {result}')
    except ValueError:
        print("Integers Only Please Try again")
        divide()
    except ZeroDivisionError:
        print(f'You can\'t divide {numerator} by zero')
    except KeyboardInterrupt:
        print('Quitting')
    except:
        print("Sorry i dont know whats up")

def main():
    divide()
main()
