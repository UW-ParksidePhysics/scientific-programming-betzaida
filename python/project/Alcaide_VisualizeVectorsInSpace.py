import numpy as np
import matplotlib.pyplot as plt
from datetime import date


N = 100
x_min, x_max = -10, 10
x = np.linspace(x_min, x_max, N)
dx = x[1] - x[0]


kinetic_energy = (-2 * np.eye(N) + np.eye(N, k=1) + np.eye(N, k=-1)) / dx**2


values, vectors = np.linalg.eigh(kinetic_energy)


lowest_indices = np.argsort(values)[:3]
eigenvalues = values[lowest_indices]
eigenvectors = vectors[:, lowest_indices]


for i in range(eigenvectors.shape[1]):
    if eigenvectors[:, i][np.argmax(np.abs(eigenvectors[:, i]))] < 0:
        eigenvectors[:, i] *= -1


plt.figure(figsize=(10, 6))
colors = ['blue', 'orange', 'green']
labels = [fr'$\psi_{i}(x), E_{{{i}}} = {eigenvalues[i]:.4f}\ \mathrm{{a.u.}}$' for i in range(3)]

for i in range(3):
    plt.plot(x, eigenvectors[:, i], label=labels[i], color=colors[i])

plt.axhline(0, color='black', linewidth=1)
plt.xlabel("Position x [a.u.]")
plt.ylabel("Wavefunction $\\psi(x)$")
plt.ylim(-2 * np.max(np.abs(eigenvectors)), 2 * np.max(np.abs(eigenvectors)))
plt.legend()


today = date.today().isoformat()
plt.text(
    -9.5,
    -0.25,
    f"Created by Betzaida Alcaide ({today})",
    fontsize=10,
    ha='left',
    va='bottom'
)

plt.title("Select Wavefunctions for a Square Potential on a Spatial Grid of 100 Points")


display_graph = True
if display_graph:
    plt.show()
else:
    plt.savefig("Betzaida_Alcaide_Square_Potential_Wavefunctions.png", dpi=300)
    plt.close()
