def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0

def read_fahrenheit_list(filename):
    """Read all Fahrenheit values starting from the 4th line."""
    with open(filename, 'r') as file:
        lines = file.readlines()[3:]
        fahrenheit_values = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 3:
                try:
                    f = float(parts[2])
                    fahrenheit_values.append(f)
                except ValueError:
                    continue
        return fahrenheit_values

def write_converted_temperatures(fahrenheit_list, output_file):
    with open(output_file, 'w') as out:
        out.write("Fahrenheit    Celsius\n")
        for f in fahrenheit_list:
            c = fahrenheit_to_celsius(f)
            out.write(f"{f:<13} {round(c, 2)}\n")

if __name__ == '__main__':
    input_file = 'temperature_data.txt'
    output_file = 'converted_temperatures.txt'

    try:
        f_values = read_fahrenheit_list(input_file)
        write_converted_temperatures(f_values, output_file)
        print(f"Converted {len(f_values)} temperatures. See '{output_file}' for results.")
    except Exception as e:
        print("Error:", e)
