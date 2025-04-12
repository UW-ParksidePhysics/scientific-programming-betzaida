import sys

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the formula:
    C = (F - 32) * 5 / 9
    """
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_fahrenheit_temperature_to_celsius_from_command_line.py <temperature_in_fahrenheit>")
    else:
        try:
            fahrenheit = float(sys.argv[1])
            celsius = fahrenheit_to_celsius(fahrenheit)
            print("Fahrenheit degrees:", fahrenheit)
            print("Celsius degrees:", round(celsius, 2))
        except ValueError:
            print("Please enter a valid number for the temperature.")
