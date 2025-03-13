print(f"{'T_F (°F)':<15}{'T_C (Exact °C)':<20}{'T_C^ (Approx. °C)':<20}")

for fahrenheit in range(-20, 121, 10):
    exact_celsius = (5/9) * (fahrenheit - 32)
    approx_celsius = (fahrenheit - 30) / 2

    print(f"{fahrenheit:<15}{exact_celsius:<20.2f}{approx_celsius:<20.2f}")
