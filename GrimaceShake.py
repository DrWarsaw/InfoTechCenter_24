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

#funtion will call the gasLevelGage to determine our gas level and then find a close gas station
# by calling the listOfGasStations function if we are on low or quarter tank

def gasLevelAlert():
    milesToGasOnLow = random.uniform(1, 25)
    milesToGasOnQT = random.uniform(25.1, 50)
    #gasLevelGauge = gasLevelGauge()
    print(milesToGasOnLow)
    print(milesToGasOnQT)

gasLevelAlert()


