<<<<<<< HEAD

=======
>>>>>>> BetaTestDev

#import libraries here
import time
import sys
timeToSleep = 2
import random
from time import sleep

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center Operating System Loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis =0
    if x ==20:
        print("\n\nOperating System Booted Up - You ARE Big Hacka Man - Access Granted!")
#Gasoline branch starts here
<<<<<<< HEAD
print("***********************")
=======
print("\n**************************\n")
>>>>>>> BetaTestDev
print("Gasoline Branch\n\n")




#Funtions that lists gas levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#funtions that lists gas station, m randomly choosing on and returning its value
def listOfGasStations():
    gasStations = ["Shell", "Speedway", "Marathon", "Circle K","Moble", "Costco", "Mijer","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return  gasStationsNearby

#funtion will call the gasLevelGage to determine our gas level and then find a close gas station
# by calling the listOfGasStations function if we are on a low or quarter tank

def gasStations():
    milesToGasOnLow = round(random.uniform(1, 25),1)
    milesToGasOnQT = round(random.uniform(25.1, 50),1)
    gasLevelPeeper= gasLevelGauge()
    if gasLevelPeeper == "Empty":
        print("*** WARNING - YOU ARE ON EMPTY")
        sleep(1.25)
        print("\n\n***Calling AAA***")
    elif gasLevelPeeper == "Low":
        print("Your gas tank is very low, checking google maps for the closest gas station.\n")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasOnLow,"miles away.")
    elif gasLevelPeeper == "Quarter Tank":
        print("Your gas tank is at a quarter of its capacity, checking google maps for the closest gas station.\n")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasOnQT,"miles away.")
    elif gasLevelPeeper == "Half Tank":
        print("Your gas tank is at a half of its capacity, you have enough gas to get to your location.\n")
    elif gasLevelPeeper == "Three Tank Quarter":
        print("Your gas tank is at three quarters of its capacity, you have more than enough "
              "gas to get to your location.\n")
    else:
        print("Your Gas tank is at full capacity no gas is needed")


gasStations()

print("\n**************************\n")

print("Weather Branch\n")


#Create a funtion that randomly chooses the weather from a list
def weather():
    weatherForcast = ["snowy", "blizzard", "raining", "foggy", "windy", "icy", "sunny"]
    weatherConditions = random.choice(weatherForcast)
    return weatherConditions


weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational weather service has updated our alarm by 30 minutes because of forcast of",weatherAlert,
              "weather conditions\n.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational weather service has updated our alarm by 45 minutes because of forcast of",weatherAlert,
              "weather conditions\n.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "raining":
        print("\nNational weather service has updated our alarm by 20 minutes because of forcast of",weatherAlert,
              "weather conditions\n.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 65mph")
    elif weatherAlert == "foggy":
        print("\nNational weather service has updated our alarm by 90 minutes because of forcast of", weatherAlert,
              "weather conditions\n.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "windy":
        print("\nNational weather service has updated our alarm by 30 minutes because of forcast of", weatherAlert,
              "weather conditions\n.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 70mph")
    elif weatherAlert == "icy":
        print("\nNational weather service has updated our alarm by 90 minutes because of forcast of", weatherAlert,
              "weather conditions\n.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 30mph")
    else:
        print("\nNational weather service gives a forcast of", weatherAlert, "weather conditions\n.")
        sleep(1.5)
        print("VRS has been disengaged have fun and be safe")



vehicleResponseSystem()

<<<<<<< HEAD
 

=======
>>>>>>> BetaTestDev
