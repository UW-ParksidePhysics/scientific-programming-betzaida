import numpy as np

# Create x_values using linspace
x_values = np.linspace(-4, 4, 100)  # 100 evenly spaced points from -4 to 4

# Compute y_values using vectorized operation
y_values = np.exp(-x_values**2)

# Optional: display to verify
if __name__ == "__main__":
    for x, y in zip(x_values, y_values):
        print(f"x = {x:.2f}, g(x) = {y:.4f}")
