def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the formula:
    C = (F - 32) * 5 / 9
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

if __name__ == "__main__":
    try:
        fahrenheit = float(input("Enter Fahrenheit temperature: "))
        celsius = fahrenheit_to_celsius(fahrenheit)

        print("Fahrenheit degrees:", fahrenheit)
        print("Celsius degrees:", round(celsius, 2))

    except ValueError:
        print("Please enter a valid number for the temperature.")