print("***********************")
print("Gasoline Branch\n\n")

#import libraries here
import random

#Funtions that lists gas levels, randomly choosing one and returing its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#funtions that lists gas station, m randomly choosing on and returning its value
def listOfGasStations():
    gasStation = ["Shell","Speedway","Marathon","Circle K","Moble","Costco","Mijer","7Eleven"]
    gasStationsNearby = random.choice(gasStation)
    return  gasStationsNearby

print(gasLevelGauge())
print(listOfGasStations())



