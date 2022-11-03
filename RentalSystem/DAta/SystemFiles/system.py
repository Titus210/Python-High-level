#!/usr/bin/python3
""" Car Rental System """



def available_cars():
    """Opens a file and returns list of available cars in the system"""
    print("\n The following cars are available:")
    try:
        with open("../Vehicles.txt", "r", encoding = "utf-8") as f:
            for data in f:
                print(data.rstrip())
    except FileNotFoundError:
        print("File opened is not found")


def rent_car():
    """Shows list of available cars to rent

        Asks reg no of car to rent
        Registers user if not in the system
        Update rentedVehicles and Customers list
    """
    # Ask registration number of car to rent
    regNumber = str(input("\nPlease Enter Registration Number of Car to rent: "))

    # Check if Car is already rented
    with open("../Vehicles.txt","r",encoding="utf-8") as f:
        for data in f:
            rowOne = data.split(",")[0]

            # Check if car is on system
            if regNumber == rowOne:
                #   Check If car is already rented
                with open("../rentedVehicles.txt","r",encoding="utf-8") as f:
                    for data in f:
                        rowOne_rented = data.split(",")[0]
                        if regNumber == rowOne_rented:
                            print(f'Sorry Car with registration number: {regNumber} is already Rented')
                            break
                        # if not rented Is available for hire
                        else:
                            print(f'Car with registration number: {regNumber} is ready for hire')

            # If car not in system return false
            else:
                print(f"Sorry! Car with registration number: {regNumber} is not found in our system")




def return_car():
    """Returns Car by registration number
        Computes amount depending on rented
        Removes car feom rented cars 
        Adds line in transaction file
    """
    print("Hello Titus you have returned car BKV-943")

def count_money():
    """Counts money in the system"""
    sum = 1 + 1
    print("{}".format(sum))

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
        rent_car()
    elif selection == 3:
        return_car()
    elif selection == 4:
        count_money()
    else:
        exit()

main()
