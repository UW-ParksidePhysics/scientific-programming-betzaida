def fahrenheit_to_celsius(fahrenheit):
        return(5/9) * (fahrenheit - 32)

fahrenheit = 0

print(f"{'F':<10}{'C':<10}")

while fahrenheit <= 100:
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit:<10}{celsius:<10.2f}")
    fahrenheit += 10