#!/usr/bin/python3
""" Returning car function """

# Ask reg Number of car to return

# Find Car in rented Vehicle first row

# Inform User If car exist or not rented

"""  Car price and account  """

# Find daily price of car in Vehicles.txt

""" Compute days """
# Get time of Car return

#  Compute number of days rented
# " number of days * price per day "

""" Delete Returned Car from Rented Vehicles.txt"""

"""Add new Line to transactions.txt"""

from datetime import datetime
def returnCar():
    # Ask registration number of car to rent
        regNumber = str(input("Please enter Registration Number of Car: "))

        # Get list of car rented and startDate of 
        regNumbers = []
        
        with open("../rentedVehicles.txt", "r", encoding="utf-8") as f:
                for data in f:
                        regRow = str(data.split(",")[0])
                        regNumbers += [regRow]
                        line = data.split(',')
                        if line[0] == regNumber:        # get start date from file
                            startDate = line[2].strip()

            
            # Get car price  and current time 
        if regNumber in regNumbers:
            with open("../Vehicles.txt", "r", encoding="utf-8") as f:
                for data in f:
                    line = data.split(',')
                    if line[0] == regNumber:
                        carPrice = int(line[2])
            
            
                 
                # convert current time to date timr format       
            timenow = datetime.now()
            returnTime = timenow.strftime("%d/%m/%Y %H:%M")

            # convert string to date

            dateStarted = datetime.strptime(startDate, '%d/%m/%Y %H:%M')
            dateReturned = datetime.strptime(returnTime, '%d/%m/%Y %H:%M')
            
            # Compute days rented
            daysRented = (dateReturned - dateStarted).days
    
            # Compute price of days rented
            price = daysRented * carPrice
            print(price)
            
        # append data to transactions file
            returnData = []
            returnData.append(regNumber)
            returnData.append(str(bDay))
            returnData.append(startDate)
            returnData.append(returnTime)
            
            # convert  list to a string
            transactionData = ",".join(returnData)
            print(transactionData)


        else:
                print("Car is not rented")
        


