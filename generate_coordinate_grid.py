a, b = 1, 2
n = 20

h = (b - a) / n

x_values_loop = []
for i in range(n + 1):
    x_values_loop.append(a + i * h)

x_values_comprehension = [a + i * h for i in range(n + 1)]

print("Using a for loop:")
print("x =", x_values_loop)

print("Using list comprehension:")
print("X =", x_values_comprehension)