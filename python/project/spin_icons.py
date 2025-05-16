"""
spin_icons.py

Final exam project script that visualizes planetary axial tilt, computes statistics,
fits a quadratic model to tilt data, and solves a characteristic matrix equation.

__author__ = "Betzaida Alcaide", "Maribel Moreno"
Date: May 12
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from scipy.stats import describe
from numpy.polynomial.polynomial import polyfit
from datetime import datetime

def get_data():
    """
    __author__ = "Betzaida Alcaide"
    Gives me the planet names and their tilt angles
    """
    return {
        'mercury': {'tilt': 0.03},
        'venus': {'tilt': 177.4},
        'earth': {'tilt': 23.4},
        'mars': {'tilt': 25.2},
        'jupiter': {'tilt': 3.1},
        'saturn': {'tilt': 26.7},
        'uranus': {'tilt': 97.8},
        'neptune': {'tilt': 28.3},
    }

def compute_tilt_statistics(planet_data):
    """
    ___author__ = "Maribel Moreno"
    Finds the average, max, min, and other stats from the tilt data
    """
    tilt_values = [info['tilt'] for info in planet_data.values()]
    return describe(tilt_values)

def fit_tilt_curve(planet_data):
    """
    ___author__ = "Betzaida Alcaide", "Maribel Moreno"
    Fits a curve to the tilt data using a quadratic equation
    """
    tilts = [info['tilt'] for info in planet_data.values()]
    indices = np.arange(len(tilts))
    coeffs = polyfit(indices, tilts, deg=2)
    return coeffs, indices, tilts

def draw_planet_icon(planet_name: str, planet_info: dict, use_color: bool = True,
                      size=(1.5, 1.5), save_path: str = None) -> None:
    """
    ___author__ = "Betzaida Alcaide", "Maribel Moreno"
    Draws a planet, its orbit, and an arrow showing the tilt
    """
    fig, ax = plt.subplots(figsize=size)
    ax.set_aspect('equal')
    ax.axis('off')

    tilt_angle = planet_info['tilt']
    angle_rad = np.radians(tilt_angle)
    radius = 1.0

    if use_color:
        planet_color = {
            'mercury': 'darkgray', 'venus': 'gold', 'earth': 'blue', 'mars': 'red',
            'jupiter': 'orange', 'saturn': 'goldenrod', 'uranus': 'lightblue', 'neptune': 'darkblue'
        }.get(planet_name, 'gray')
        tilt_color = 'yellow'
    else:
        planet_color = 'gray'
        tilt_color = 'black'

    # Horizontal orbit reference line
    ax.plot([-2.5, 2.5], [0, 0], linestyle='--', color='gray', lw=0.8)

    # Draw planet
    ax.add_patch(plt.Circle((0, 0), radius, color=planet_color, ec='black', zorder=2))

    # Rotational axis
    ax.plot([0, 0], [-1.5 * radius, 1.5 * radius], color='black', lw=1.2)

    # Tilt vector
    x_tilt = radius * np.sin(angle_rad)
    y_tilt = radius * np.cos(angle_rad)
    arrow = FancyArrowPatch((0, 0), (x_tilt, y_tilt), arrowstyle='->', color=tilt_color, lw=2.0, mutation_scale=15)
    ax.add_patch(arrow)

    # Arc for tilt angle
    arc_radius = 0.5  # Explicitly define arc radius before use
    arc_angles = np.linspace(0.0, angle_rad, 50)  # Ensure float value in linspace
    arc_x = arc_radius * np.sin(arc_angles)
    arc_y = arc_radius * np.cos(arc_angles)
    ax.plot(arc_x, arc_y, color='black', lw=1.0)

    # Angle label
    label_x = arc_radius * np.sin(angle_rad / 2.0)
    label_y = arc_radius * np.cos(angle_rad / 2.0)
    ax.text(label_x, label_y, f"{tilt_angle:.0f}°", fontsize=8, ha='left', va='bottom')

    # Rotation arrow around equator
    theta1 = np.radians(60)
    theta2 = np.radians(300)
    arc_arrow = FancyArrowPatch(
        (radius * np.cos(theta1), radius * np.sin(theta1)),
        (radius * np.cos(theta2), radius * np.sin(theta2)),
        connectionstyle="arc3,rad=0.5", arrowstyle='->', color='black', lw=1.0, mutation_scale=10
    )
    ax.add_patch(arc_arrow)

    # Timestamp
    timestamp = datetime.now().strftime("Created on %Y-%m-%d")
    ax.text(-2.4, -2.6, timestamp, fontsize=6, ha='left')

    ax.set_title(f"{planet_name.capitalize()}\n{tilt_angle:.0f}°", fontsize=10)

    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.close()

def matrix_demo() -> tuple[np.ndarray, np.ndarray]:
    """
    ___author__ = "Maribel Moreno"
    Builds a 10x10 matrix like in the matrix assignment, solves for eigenvalues and eigenvectors, and prints the results
    """
    n = 10
    main_diag = 2 * np.ones(n)
    off_diag = -1 * np.ones(n - 1)

    # Construct symmetric tridiagonal matrix
    H = np.diag(main_diag) + np.diag(off_diag, 1) + np.diag(off_diag, -1)
    H *= 1 / (2 * (1 / (n + 1)) ** 2)

    eigenvalues, eigenvectors = np.linalg.eig(H)
    idx = np.argsort(eigenvalues)
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    print("\nEigenvalues (lowest to highest):\n", eigenvalues)
    print("\nEigenvectors (each column matches eigenvalue above):\n", eigenvectors)

    return eigenvalues, eigenvectors

def main() -> None:
    """
    __author__ = "Betzaida Alcaide"
    """
    data = get_data()
    stats = compute_tilt_statistics(data)
    print("\nTilt Statistics:", stats)

    coeffs, x_vals, y_vals = fit_tilt_curve(data)
    fit_x = np.linspace(0, len(x_vals) - 1, 100)
    fit_y = sum(c * fit_x ** i for i, c in enumerate(coeffs))

    plt.figure()
    plt.plot(x_vals, y_vals, 'o', label='Data')
    plt.plot(fit_x, fit_y, '-', label='Quadratic Fit')
    plt.title('Axial Tilt Fit')
    plt.xlabel('Planet Index')
    plt.ylabel('Tilt (°)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("tilt_fit_plot.png")
    plt.close()

    for planet, info in data.items():
        draw_planet_icon(planet, info, use_color=True, save_path=f"{planet}_tilt.png")

    matrix_demo()

if __name__ == "__main__":
    main()