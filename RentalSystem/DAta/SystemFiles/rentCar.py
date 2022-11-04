#!/usr/bin/python3

#---------------------------------------
#          Car Details    
#---------------------------------------
from datetime import datetime
import re
import math
def car_to_rent():
    # Ask registration number of car to rent
    regNumber = str(input("Please enter Registration Number of Car"))
    print(regNumber)

    # Check if Car is already rented
    regNumbers = []
    with open("../Vehicles.txt", "r", encoding="utf-8") as f:
        for data in f:
            regRow = str(data.split(",")[0])
            regNumbers += [regRow]
    if regNumber in regNumbers:
        regVehicle = []
        with open("../rentedVehicles.txt", "r", encoding="utf-8") as f:
            for cars in f:
                regRow = str(cars.split(",")[0])
                regVehicle += [regRow]
        if regNumber in regVehicle:
            print("Car is Rented")
        else:
            validate_Birthday()
    else:
        print("Car not in the system")



#------------------------------------------------
#       Customer Details   
#------------------------------------------------

# Validate Date
import math
import re
import time
def validate_Birthday():
    Result = None
    while True:
        # Ask Customer Birthday
        bDay = input("Please Enter you BirthDay in format: dd/mm/yyyy: ")
        # Check if birthday is given in right format (DD/MM/YYY)
        try:
            date = time.strptime(bDay, "%d/%m/%Y")
            result = True
            break
        except ValueError:
            print(f"Sorry!, {bDay} is invalid date!")
            result = False
            continue

        # Check If date and year is valid (dd < 31, mm <= 12, yyyy <= 2022)
    if result == True:
        regex = re.search(
            r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$', bDay)
        if regex:
            striped_time = datetime.strptime(bDay, '%m/%d/%Y')
            age = ((datetime.today() - striped_time).days / 365)

        # Check if age is <= 100  and age is >= 18
            if age >= 18 and age <= 100:
                print("Eligible")

            else:
                print("Not Eligible!")
                validate_Birthday()
        else:
            print("Enter A vald date format")
            validate_Birthday()


car_to_rent()






"""      Customers Availability  """

# Add Birthday, first name, last name , email address:right format to Customer.txt file

""" Renting Car     """

# Add Car Reg No, Birthday, timestamp(started) to rentedVehicles.txt

"""     Display Confirmation    """

# Display First name and Rented Car reg Number
