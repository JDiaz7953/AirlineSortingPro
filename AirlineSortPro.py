
# Project Description:
# --------------------
# This Program will be able to display information about
# Flights leaving from Providence to Orlando the user will
# be able to get information such as what specific flight 
# they want, finding the cheapest flight, and being able
# find the average price of tickets for all flights and more

# Function that allows the user to type in a file they would like to use & correct the user if the file is Invalid
def openFile():
    goodFile = False
    while goodFile == False:
        fName = input("Please enter a file name: ")
        try: 
            gradFile = open(fName,"r")
            goodFile = True
        except IOError:
            print("Invalid file name try again... ")
    return gradFile

# get the data from the csv file and sorts all data in the correct list 
def getData():
    airlineSchedule = openFile()
    airlineList = []
    flightNumberList = []
    departureTimeList = []
    arrivalTimeList = []
    priceList = []
    for line in airlineSchedule:
        line = line.strip()
        airline, flightNumber, departure, arrival,price = line.split(",")
        airlineList.append(airline)
        flightNumberList.append(flightNumber)
        departureTimeList.append(departure)
        arrivalTimeList.append(arrival)
        priceList.append(price)
    airlineSchedule.close()
    return airlineList, flightNumberList, departureTimeList,arrivalTimeList, priceList
    
    #This function displays the menu of choices for the user
    #It reads in the user's choice and returns it as an integer
def getChoice():
    print("")
    print("Please choose one of the following options:")
    print("1 -- Find flight information by airline and flight number")
    print("2 -- Find flights shorter than a specified duration")
    print("3 -- Find the cheapest flight by a given airline")
    print("4 -- Find flight departing after a specified time")
    print("5 -- Find the average price of all flights")
    print("6 -- Write a file with flights sorted by departure time")
    print("7 -- Quit")
    OK = False
    while OK == False:
        try:
            choice = int(input("Choice ==> "))
            if choice >= 0 and choice <= 7:
                OK = True
            else:
                print("Entry must be between 1 and 7")
        except ValueError:
            print("Entry must be a number")
    print("")
    return choice

#Informs the user the flight number picked is not a valid option if the flight number does not exist
def exception(flightNumberList):
   OK = False
   while OK == False:
       try:
           flightNumber = input("Enter flight number: ")
           if flightNumber in flightNumberList:
                OK = True 
           else:
                print("Invalid input -- try again")
       except ValueError:
           print("Invalid entry, try again... ")
   return flightNumber

#Informs the user the airline picked is not a valid option if the airline does not exist
def exceptionAirline(airlineList):
   OK = False
   while OK == False:
       try:
           airlineName = input("Enter airline name: ")
           if airlineName in airlineList:
                OK = True 
           else:
                print("Invalid input -- try again")
       except ValueError:
           print("Invalid entry, try again... ")
   return airlineName

#Finds the specifc flight a user is searching for using the airline and flight numbers
def findSpecificFlight(airlineList,flightNumberList):
    airlineName = exceptionAirline(airlineList)
    flightNumber = exception(flightNumberList)
    #searches for the flight number and airline the user is searching for and then returns the index of that flight
    for i in range(len(flightNumberList)):
        if flightNumberList[i] == flightNumber and airlineList[i] == airlineName:
            index = i
            return index
    return -1
     
#This functions tells the user the entry must be a number in the case a letter is used by accident 
def exceptionSpecifedFlight():
   OK = False
   while OK == False:
       try:
           maxDur = int(input("Enter maximum duration (in minutes): "))
           if maxDur != "" :
                OK = True 
       except ValueError:
           print("Entry must be a number")
   return maxDur

#finds shorter than specifed flights
def shorterThanSpecified(arrivalTimeList,departureTimeList):
    flightIndexList = []
    durationList = []
    arrivalInMin = []
    departInMin = []
    maxDur = exceptionSpecifedFlight()
    #Converts the time in the arrival time list from military time to minutes and adds it to a new list that has all of the arival time in minutes
    for i in arrivalTimeList:
        hour, minute = i.split(":")
        hourToMin = int(hour) * 60
        timeInMinutes = int(hourToMin) + int(minute)
        arrivalInMin.append(timeInMinutes)
    
    #Converts the time in the departure time list from military time to minutes and adds it to a new list that has all of the departure time in minutes
    for i in departureTimeList:
        hour, minute = i.split(":")
        hourToMin = int(hour) * 60
        timeInMinutes = int(hourToMin) + int(minute)
        departInMin.append(timeInMinutes)
    
    #gets the total duration of each flight and adds it a list
    for i in range(len(arrivalTimeList)):
       duration = int(arrivalInMin[i]) - int(departInMin[i])
       durationList.append(duration)
    
    #finds the index of each flight that is less than or equal to the user input then adds it to the flight index list
    for i in range(len(durationList)):
        if durationList[i] <= maxDur: 
            flightIndexList.append(i)
    
    return flightIndexList

#This functions finds the cheapest flight in a specific airline
def theCheapestFlight(airlineList,priceList):
    newPriceList = []
    airlinePriceindex = []
    airlineName = exceptionAirline(airlineList) 
    
    #gets the index of all the flights of a specific airline the user is requesting for and adds it to a list
    for i in range(len(airlineList)):
        if airlineList[i] == airlineName:
            airlinePriceindex.append(i)
    
    #takes all the prices in price list and converts it to a integer, then adds it to a list with all the prices being a tnteger
    for i in priceList:
        dollarSign, price = i.split("$")
        intPrice = int(price)
        newPriceList.append(intPrice)
    
    lowestPrice = newPriceList[28]
    #searches through the list of indexes of the specfic flights, Then uses those index to search through the new price list to obtain the lowest price
    for i in airlinePriceindex:
        if newPriceList[i] < lowestPrice:
           lowestPrice = newPriceList[i]
           index = i
    return index




#Finds the flights that depart after a specific time 
def flightDepartAfterSpecTime(arrivalTimeList,departureTimeList):
    departInMin = []
    departFlightIndexList = [] 
    specTime = input("Enter earliest departure time: ")
    
    #Checks to see if the input the user is valid
    OK = False
    while OK == False:
        if len(specTime) == 5:
         try:
            hour, minute = specTime.split(":")
            if int(hour) >= 0 and int(hour) <= 24 and int(minute) >= 0 and int(minute) <= 60:
                 OK = True
         except ValueError:
            specTime = input("Invalid time - Try again ")
        
        if OK == False:
            specTime = input("Invalid time - Try again ")
    
    #converts the time the user inputted to mintues 
    hourToMin = int(hour) * 60
    specTimeInMinutes = int(hourToMin) + int(minute)
   
   #Converts the time in the departure time list from military time to minutes and adds it to a new list that has all of the departure time in minutes
    for i in departureTimeList:
        hour, minute = i.split(":")
        hourToMin = int(hour) * 60
        timeInMinutes = int(hourToMin) + int(minute)
        departInMin.append(timeInMinutes)
   
    #compares all the departure time in minutes to the users time, if the departure time is greater than the user time the index of that flight is added to the list
    for i in range(len(departureTimeList)):
        if departInMin[i] > specTimeInMinutes:
             departFlightIndexList.append(i)
    
    return departFlightIndexList

#Gets the average price for all flights
def flightAveragePrice(priceList):
    newPriceList = []
    sum = 0
    #converts the prices in priceList from strings to Integers and adds it to a new list with prices being a integer
    for i in priceList:
        dollarSign, price = i.split("$")
        intPrice = int(price)
        newPriceList.append(intPrice)
    
    #summates all the prices in the new price list 
    for i in range(len(newPriceList)):
        sum = sum + newPriceList[i]
   
   #converts the sum of all prices and gets the average, then converts the average price back in to a string 
    averagePrice = float(sum) / len(priceList)
    averagePrice = "{:,.2f}".format(averagePrice)
    averagePrice = str(averagePrice)
    averagePrice = '$' + averagePrice
    
    return averagePrice
   
def selectionSort(departureTimeList):
    indexList = []
    departWholeNum = []
    for i in range(len(departureTimeList)):
        departTime = departureTimeList[i].replace(":","")
        wholeNum = int(departTime)
        departWholeNum.append(wholeNum)
        indexList.append(i)
    
    for i in range(0, len(departWholeNum)):            
        min = i
        for j in range(i + 1, len(departWholeNum)):
            # comparison
            if  departWholeNum[j] < departWholeNum[min]:
                min = j
        # swap
        departWholeNum[i],  departWholeNum[min] =  departWholeNum[min],  departWholeNum[i]
        indexList[i],  indexList[min] =  indexList[min],  indexList[i]
    return  indexList
  
def outputFile(airlineList, flightNumberList, departureTimeList,arrivalTimeList, priceList,indexList):
 outFile = open("time-sorted-flights.csv", 'w')
 for i in indexList:
        outFile.write(airlineList[i] + "," + flightNumberList[i] + "," + departureTimeList[i] + "," + arrivalTimeList[i]+","+priceList[i] + '\n')
        i = i + 1
 outFile.close()
 print("Sorted data has been written to file: time-sorted-flights.csv")

 return


def main():
    
    airlineList, flightNumberList, departureTimeList,arrivalTimeList, priceList =  getData()
    choice = getChoice()
    while choice != 7:
        
        if choice == 1:
            index = findSpecificFlight(airlineList,flightNumberList)
            if index == -1:
                print("")
                print("No flight meets your criteria")
                choice = getChoice()
            else:
                print("")
                print("The flight that meets your criteria is:")
                print("")
                print("AIRLINE  FLT#     DEPART  ARRIVE PRICE   ")
                print(airlineList[index].ljust(8), flightNumberList[index].ljust(6), departureTimeList[index].rjust(7), arrivalTimeList[index].rjust(7), priceList[index].rjust(3))
                choice = getChoice()
        
        if choice == 2:
            flightIndexList = shorterThanSpecified(arrivalTimeList,departureTimeList)
            if flightIndexList == []:
                print("")
                print("No flights meet your criteria")
                choice = getChoice()
            else:
                print("")
                print("The flights that meet your criteria are: ")
                print("")
                print("AIRLINE  FLT#     DEPART  ARRIVE PRICE   ")
                for index in flightIndexList:
                 print(airlineList[index].ljust(8), flightNumberList[index].ljust(6), departureTimeList[index].rjust(7), arrivalTimeList[index].rjust(7), priceList[index].rjust(5))
                choice = getChoice()
        
        if choice == 3:
           index = theCheapestFlight(airlineList,priceList)
           print("")
           print("The flight that meets your criteria is:")
           print("")
           print("AIRLINE  FLT#     DEPART  ARRIVE PRICE   ")
           print(airlineList[index].ljust(8), flightNumberList[index].ljust(6), departureTimeList[index].rjust(7), arrivalTimeList[index].rjust(7), priceList[index].rjust(5))
           choice = getChoice()
        
        if choice == 4:
            departFlightIndexList = flightDepartAfterSpecTime(arrivalTimeList,departureTimeList)
            if departFlightIndexList == []:
                print("")
                print("No flights meet your criteria")
                choice = getChoice()
            else:
                    print("")
                    print("The flights that meet your criteria are:")
                    print("")
                    print("AIRLINE  FLT#     DEPART  ARRIVE PRICE   ")
                    for index in departFlightIndexList:
                       print(airlineList[index].ljust(8), flightNumberList[index].ljust(6), departureTimeList[index].rjust(7), arrivalTimeList[index].rjust(7), priceList[index].rjust(5))
                    choice = getChoice()
        
        if choice == 5:
            averagePrice = flightAveragePrice(priceList)
            print("The average price is", averagePrice )
            choice = getChoice() 
        
        if choice == 6:
             indexList = selectionSort(departureTimeList)
             outputFile(airlineList, flightNumberList, departureTimeList,arrivalTimeList, priceList,indexList)
             choice = getChoice()

    if choice == 7:
        print("")
        print("Thank you for flying with us")



            


