#!/usr/bin/python3

#---------------------------------------
#          Car Details    
#---------------------------------------
def car_to_rent():
# Ask registration number of car to rent
    regNumber = str(input("\nPlease Enter Registration Number of Car to rent: "))

# Check if Car is already rented
    with open("../Vehicles.txt", "r", encoding="utf-8") as f:
        for data in f:
            rowOne = data.split(",")[0]

           # Check if car is on system
            if regNumber == rowOne:
                # Check If car is already rented
                with open("../rentedVehicles.txt", "r", encoding="utf-8") as f:
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
                print("Sorry! Car with registration number: {regNumber} is not found in our system")



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
