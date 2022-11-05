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
                            bDay = line[1]

            
            # Get car price  and current time 
        if regNumber in regNumbers:
            with open("../Vehicles.txt", "r", encoding="utf-8") as f:
                for data in f:
                    line = data.split(',')
                    if line[0] == regNumber:
                        carPrice = int(line[2])
            
            
                 
                # convert current time to date time format       
            timenow = datetime.now()
            returnTime = timenow.strftime("%d/%m/%Y %H:%M")

            # convert string to date

            dateStarted = datetime.strptime(startDate, '%d/%m/%Y %H:%M')
            dateReturned = datetime.strptime(returnTime, '%d/%m/%Y %H:%M')
            
            # Compute days rented
            daysRented = (dateReturned - dateStarted).days
    
            # Compute price of days rented
            price = format(daysRented * carPrice, ".2f")
         

            returnData = []
            returnData.append(regNumber)
            returnData.append(bDay)
            returnData.append(startDate)
            returnData.append(returnTime)
            returnData.append(str(price))
            
            # convert  list to a string
            transactionData = ",".join(returnData)

        # append data to transactions file
            with open("../transActions.txt","a+",encoding="utf-8") as f:
                f.seek(0,2)
                # append next line if not empty
                f.write(transactionData)
                f.write("\n")
                        
        # remove line from rentedVehicles.txt
                with open("../rentedVehicles.txt", "r+", encoding="utf-8") as f:
                        file = f.readlines() 
                        f.seek(0)
                        for line in file:
                                if not line.startswith(regNumber):
                                        f.write(line)
                        f.truncate()

                
        else:
                print("Car is not rented")
        

returnCar()
