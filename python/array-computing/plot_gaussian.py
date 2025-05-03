import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x_values = np.linspace(-4, 4, 200)
y_values = np.exp(-x_values**2)

# Plot the function
plt.plot(x_values, y_values, label=r'$g(x) = e^{-x^2}$', color='blue')
plt.title("Gaussian Function")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.grid(True)
plt.legend()
plt.savefig("gaussian_plot.png")  # Saves the figure
plt.show()
