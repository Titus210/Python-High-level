#!/usr/bin/python3
""" Car Rental System """
import sys
import returnCar
import rentCar
import countMoney


def available_cars():
    """Opens a file and returns list of available cars in the system"""
    print("\n The following cars are available:")
    try:
        with open("../Vehicles.txt", "r", encoding="utf-8") as f:
            for data in f:
                print(data.rstrip())
    except FileNotFoundError:
        print("File opened is not found")

def main():
    """Menu to show  the sysyem operations"""
    print("\n Welcome to Car Rental System\n")

    # Display operation Menu
    print("You may select one of the following:")
    print(" 1. List available cars\n 2. Rent a Car\n 3. Return a car\n 4. Count the money\n 0. Exit")

    #Prompt User to enter Choise from menu
    selection = 0
    selection = int(input("\nWhat is your selection: "))

    # Open Operation functions based on selection
    if selection == 1:
        available_cars()
    elif selection == 2:
        rentCar.car_to_rent()
    elif selection == 3:
        returnCar.returnCar()
    elif selection == 4:
        print("counting")
    else:
        sys.exit("Exiting.....")

main()
