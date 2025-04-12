def convert_fahrenheit_to_celsius(fahrenheit_temperature):
    """
    Convert Fahrenheit to Celsius using the formula:
    C = (F - 32) * 5 / 9
    """
    celsius_temperature = (fahrenheit_temperature - 32) * 5.0 / 9.0
    return celsius_temperature

def convert_celsius_to_fahrenheit(celsius_temperature):
    """
    Convert Celsius to Fahrenheit using the formula:
    F = (9/5) * C + 32
    """
    fahrenheit_temperature = (9.0 / 5.0) * celsius_temperature +32
    return fahrenheit_temperature

if __name__ == '__main__':
    celsius_values = [0, 21, 100]

    print("Celsius to Fahrenheit and Back to Celsius:")
    print("Celsius -> Fahrenheit -> Back to Celsius")

    for celsius in celsius_values:
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        converted_celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(str(celsius) + " C -> " + str(round(fahrenheit, 2)) + " F -> " + str(round(converted_celsius, 2)) + " C")