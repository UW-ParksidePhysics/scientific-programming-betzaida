def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the formula:
    C = (F - 32) * 5 / 9
    """
    return (fahrenheit - 32) * 5.0 / 9.0

def read_fahrenheit_from_file(filename):
    """
    Read Fahrenheit temperature from a file by skipping the first three lines,
    then extracting the third word from the fourth line.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        if len(lines) < 4:
            raise ValueError("File does not contain enough lines.")
        line = lines[3]
        words = line.strip().split()
        if len(words) < 3:
            raise ValueError("The fourth line does not contain enough words.")
        return float(words[2])

if __name__ == '__main__':
    filename = 'temperature_data.txt'
    try:
        fahrenheit = read_fahrenheit_from_file(filename)
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("Fahrenheit degrees:", fahrenheit)
        print("Celsius degrees:", round(celsius, 2))
    except Exception as e:
        print("Error:", e)