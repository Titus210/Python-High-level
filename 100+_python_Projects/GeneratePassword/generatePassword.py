import random


def getName():
    name = input("Enter your name: ")
    try:
        passwordLength = input("Enter your password length: ")
    except ValueError:
        print("Enter an integer value for your password length")
        getName()

    return name, passwordLength


def generatePassword(passwordLength):
    sample = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    password = "".join(random.sample(sample, passwordLength))

    return password


def main(passwordLength, password):
    getName()
    generatePassword(passwordLength)
    print(f"Your password is: {password}")

