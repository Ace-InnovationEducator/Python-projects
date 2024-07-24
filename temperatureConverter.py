import random
from colorama import Fore
from itertools import chain

red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
black = Fore.BLACK

def temperatureGaugeConverter(temperature):
    FAHRENHEIT_TO_CELSIUS = (temperature - 32) * (5/9)
    #CELSIUS_TO_FAHRENHEIT = 20
    
    
    if(temperature >= 90):
        print("Fahrenheit: ", red, "{0:4.1f}".format(temperature), black)
        print("Celsius: ", red, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)
    elif(temperature <= 89) & (temperature >= 75):
        print("Fahrenheit: ", yellow, "{0:4.1f}".format(temperature), black)
        print("Celsius: ", yellow, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)
    elif(temperature <= 74) & (temperature >= 67):
        print("Fahrenheit: ", green, "{0:4.1f}".format(temperature), black)
        print("Celsius: ", green, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), green, black)
    elif(temperature <= 66):
        print("Fahrenheit: ", blue, "{0:4.1f}".format(temperature), black)
        print("Celsius: ", blue, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)

    print()

for x in range(5):
    user_input = float(input("Enter a temperature to convert from Fahrenheit to Celsius:  "))
    temperatureGaugeConverter(user_input)



#temperatureGaugeConverter(93)
#temperatureGaugeConverter(84)
#temperatureGaugeConverter(72)
#temperatureGaugeConverter(55)