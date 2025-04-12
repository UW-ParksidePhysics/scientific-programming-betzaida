import sys

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def test_conversion():
    tol = 1e-6
    f = 77.0
    c = 25.0
    k = 298.15

    assert abs(celsius_to_fahrenheit(fahrenheit_to_celsius(f)) - f) < tol
    assert abs(fahrenheit_to_celsius(celsius_to_fahrenheit(c)) - c) < tol
    assert abs(celsius_to_kelvin(kelvin_to_celsius(k)) - k) < tol
    assert abs(kelvin_to_celsius(celsius_to_kelvin(c)) - c) < tol
    assert abs(kelvin_to_fahrenheit(fahrenheit_to_kelvin(f)) - f) < tol
    assert abs(fahrenheit_to_kelvin(kelvin_to_fahrenheit(k)) - k) < tol
    print("All conversion tests passed.")

def main():
    if len(sys.argv) >= 2 and sys.argv[1] == 'verify':
        test_conversion()
        return

    if len(sys.argv) != 3:
        print("Usage: python convert_temperature.py <value> <unit>")
        print("Example: python convert_temperature.py 21.3 C")
        return

    try:
        temp = float(sys.argv[1])
        unit = sys.argv[2].upper()

        if unit == 'C':
            f = celsius_to_fahrenheit(temp)
            k = celsius_to_kelvin(temp)
            print(f"{f:.1f} F {k:.1f} K")
        elif unit == 'F':
            c = fahrenheit_to_celsius(temp)
            k = fahrenheit_to_kelvin(temp)
            print(f"{c:.1f} C {k:.1f} K")
        elif unit == 'K':
            c = kelvin_to_celsius(temp)
            f = kelvin_to_fahrenheit(temp)
            print(f"{c:.1f} C {f:.1f} F")
        else:
            print("Unknown unit. Use C, F, or K.")
    except ValueError:
        print("Invalid temperature value.")

if __name__ == '__main__':
    main()
