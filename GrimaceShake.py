print("\n**************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a funtion that randomly chooses the weather from a list
def weather():
    weatherForcast = ["snowy", "blizzard", "raining", "foggy", "windy", "icy", "sunny"]
    weatherConditions = random.choice(weatherForcast)
    return weatherConditions


weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational weather service has updated our alarm by 30 minutes because of forcast of",weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational weather service has updated our alarm by 45 minutes because of forcast of",weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "raining":
        print("\nNational weather service has updated our alarm by 20 minutes because of forcast of",weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 65mph")
    elif weatherAlert == "foggy":
        print("\nNational weather service has updated our alarm by 90 minutes because of forcast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "windy":
        print("\nNational weather service has updated our alarm by 30 minutes because of forcast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 70mph")
    elif weatherAlert == "icy":
        print("\nNational weather service has updated our alarm by 90 minutes because of forcast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 30mph")
    else:
        print("\nNational weather service gives a forcast of", weatherAlert, "weather conditions.")
        sleep(1.5)
        print("VRS has been disengaged have fun and be safe")






vehicleResponseSystem()