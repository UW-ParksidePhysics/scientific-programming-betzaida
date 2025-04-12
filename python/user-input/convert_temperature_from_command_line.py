import sys

def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0

if __name__ == '__main__':
    try:
        # Attempt to get the Fahrenheit value from the command line
        fahrenheit = float(sys.argv[1])
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("Fahrenheit degrees:", fahrenheit)
        print("Celsius degrees:", round(celsius, 2))

    except IndexError:
        print("Error: Missing Fahrenheit temperature on the command line.")
        print("Usage: python convert_temperature_from_command_line.py <temperature_in_fahrenheit>")

    except ValueError:
        print("Error: Temperature must be a valid number.")