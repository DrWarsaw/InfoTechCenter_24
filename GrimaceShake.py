print("\n**************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a funtion that randomly chooses the weather from a list
def weather():
    weatherForcast = ["Snowing", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunny"]
    weatherConditions = random.choice(weatherForcast)
    return weatherConditions


print(weather())