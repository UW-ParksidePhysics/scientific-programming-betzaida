import numpy as np
import matplotlib.pyplot as plt
from generate_matrix import generate_matrix
from datetime import datetime


potential_type = 'square'
num_points = 90
potential_parameter = 1
x_min, x_max = -2, 2
selected_indices = [0, 1, 2]


H = generate_matrix(x_min, x_max, num_points, potential_type, potential_parameter)


eigenvalues, eigenvectors = np.linalg.eigh(H)
x_values = np.linspace(x_min, x_max, num_points)


plt.figure(figsize=(8, 6))
for i in selected_indices:
    plt.plot(x_values, eigenvectors[:, i], label=f"$\\psi_{{{i}}}(x)$")

plt.xlabel("Position $x$")
plt.ylabel("Wavefunction $\\psi(x)$")
plt.title("Betzaida Alcaide – Square Potential Eigenfunctions")
plt.grid(True)
plt.legend()


today = datetime.today().strftime('%Y-%m-%d')
plt.text(0.01, 0.01, f"Created by Betzaida Alcaide ({today})", transform=plt.gca().transAxes,
         fontsize=8, ha='left', va='bottom')


plt.savefig("Alcaide_SquarePotential_Eigenfunctions.png", dpi=300)
plt.show()
