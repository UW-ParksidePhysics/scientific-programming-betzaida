import numpy as np

# Define the x range (as in Exercise 5.1)
start = -4
end = 4
num_points = 100  # Adjust for resolution

# Create empty arrays
x_values = np.zeros(num_points)
y_values = np.zeros(num_points)

# Fill with a for loop
for i in range(num_points):
    x = start + i * (end - start) / (num_points - 1)
    x_values[i] = x
    y_values[i] = np.exp(-x**2)  # g(x) = e^(-x^2)

# Optional: print to verify
if __name__ == "__main__":
    for x, y in zip(x_values, y_values):
        print(f"x = {x:.2f}, g(x) = {y:.4f}")
