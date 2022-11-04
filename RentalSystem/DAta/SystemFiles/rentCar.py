#!/usr/bin/python3

#---------------------------------------
#          Car Details    
#---------------------------------------
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
        print(regVehicle)
        if regNumber in regVehicle:
            print("Car is Rented")
        else:
            print("Car Availabile")
    else:
        print("Car in the system")



#------------------------------------------------
#       Customer Details   
#------------------------------------------------

# Validate Date
import time
def validate_Birthday():
    Result = None
    while True:
        # Ask Customer Birthday
        bDay = input("Please Enter you BirthDay in format: dd/mm/yyyy: ")
        # Check if birthday is given in right format (DD/MM/YYY)
        try:
            date = time.strptime(bDay, "%d/%m/%Y")
            print(f"Your Birthday is: {bDay}")
            result = True
            break
        except ValueError:
            print(f"Sorry!, {bDay} is invalid date!")
            result = False
            continue
    return result




# Date is sensible (Date 30/31 days and month 12) 

# Check if age range ( less than 100) and (greater or equal to 18 from 2022)


"""      Customers Availability  """

# Add Birthday, first name, last name , email address:right format to Customer.txt file

""" Renting Car     """

# Add Car Reg No, Birthday, timestamp(started) to rentedVehicles.txt

"""     Display Confirmation    """

# Display First name and Rented Car reg Number
