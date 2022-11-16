from math import sin
import turtle


def base_height():
    base = int(input("Please enter the base length "))
    height = int(input("Please enter the height : "))

    area = base * height
    print(f"Area of pallalelogram is {area}")

def angle_base():
    base = int(input("Please enter the base length "))
    height = int(input("Please enter the height : "))
    angle = int(input("Please enter the angle : "))

    area = base * height * sin(angle)
    print(f"Area of pallalelogram is {area:.2f}")
    

def main():

    print("Do you have one side angle?")

    option = int(input("1. Yes \n2. No \n"))
    if option == 1:
        angle_base()
    elif option == 2:
        base_height()

    else:
        print("Incorrect option")

main()
