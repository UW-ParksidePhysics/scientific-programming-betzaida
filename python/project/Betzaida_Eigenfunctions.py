import numpy as np
import matplotlib.pyplot as plt
from generate_matrix import generate_matrix

min_x = -2
max_x = 2
num_points = 90
potential_name = 'square'
potential_parameter = 1
eigen_indices = [0, 1, 2]

H = generate_matrix(min_x, max_x, num_points, potential_name, potential_parameter)

eigenvalues, eigenvectors = np.linalg.eigh(H)

x_vals = np.linspace(min_x, max_x, num_points)

plt.figure(figsize=(8, 6))

for i in eigen_indices:
    plt.plot(x_vals, eigenvectors[:, i], label=f'ψ_{i}(x)')

plt.title("Alcaide - Eigenfunctions from Square Potential")
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.legend()
plt.grid(True)

plt.savefig("Alcaide_SquarePotential_Eigenfunctions.png", dpi=300)
plt.show()
