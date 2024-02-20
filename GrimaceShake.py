print("***********************")
print("Gasoline Branch\n\n")

#import libraries here
import random
from time import sleep

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
    milesToGasOnLow = round(random.uniform(1, 25),1)
    milesToGasOnQT = round(random.uniform(25.1, 50),1)
    gasLevel= gasLevelGauge()
    if gasLevel == "Empty":
        print("*** WARNING - YOU ARE ON EMPTY")
        sleep(1.25)
        print("\n\n***Calling AAA***")

gasLevelAlert()


 