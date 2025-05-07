import numpy as np
import matplotlib.pyplot as plt

# Matrix dimension
matrix_dimension = 10
n = matrix_dimension

# Constructing matrix H
main_diag = 2 * np.ones(n)
off_diag = -1 * np.ones(n - 1)

H = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
scaling_factor = 1 / (2 * (1 / (n + 1)) ** 2)
H = scaling_factor * H

# Computing eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(H)

# Sorting eigenvalues and eigenvectors
i_sorted = np.argsort(eigenvalues)
eigenvalues = eigenvalues[i_sorted]
eigenvectors = eigenvectors[:, i_sorted]

# Defining x values and sine function
x_values = np.linspace(1 / (n + 1), n / (n + 1), n)
sine_function = np.sqrt(2) * np.sin(np.pi * x_values)

# Plotting fifth eigenvector (index 4)
plt.plot(x_values, eigenvectors[:, 4], label="5th Eigenvector")
plt.plot(x_values, sine_function, '--', label=r"$\sqrt{2} \sin(\pi x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.title("5th Eigenvector vs $\\sqrt{2}\\sin(\\pi x)$ for n=10")
plt.legend()
plt.grid(True)
plt.show()
