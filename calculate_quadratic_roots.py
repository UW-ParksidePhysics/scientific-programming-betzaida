import numpy as np
from numpy.lib.scimath import sqrt

def convert_fahrenheit_to_celsius(fahrenheit_temperature):
    """
    Convert Fahrenheit to Celsius using the formula:
    C = (F - 32) * 5 / 9
    """
    celsius_temperature = (fahrenheit_temperature - 32) * 5 / 9
    return celsius_temperature

def convert_celsius_to_fahrenheit(celsius_temperature):
    """
    Convert Celsius to Fahrenheit using the formula:
    F = (C - 32) * 5 / 9
    """
    fahrenheit_temperature = (9 /5) * celsius_temperature + 32
    return fahrenheit_temperature

if __name__ == "__main__":
    celsius_values = [0, 21, 100]

    print("Celsius -> Fahrenheit -> Celsius (after conversion)")
    print ("_____________________________________________")

    for celsius in celsius_values:
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        converted_celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(str(celsius) + " C -> " + str(round(fahrenheit, 2)) + "F -> " + str(round(converted_celsius,2)) + " C")

        print("\nDemostrating scimath.sqrt for positive and negative values:")
        example_values = [4, -4, 0, 9, -9]
        for value in example_values:
            sqrt_value = sqrt(value)
            print("sqrt(" + str(value) + ") = " + str(sqrt_value))