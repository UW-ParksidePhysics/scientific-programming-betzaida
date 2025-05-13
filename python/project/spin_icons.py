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
    planet_data = {
        'mercury': {'tilt': 0.03},
        'venus': {'tilt': 177.4},
        'earth': {'tilt': 23.4},
        'mars': {'tilt': 25.2},
        'jupiter': {'tilt': 3.1},
        'saturn': {'tilt': 26.7},
        'uranus': {'tilt': 97.8},
        'neptune': {'tilt': 28.3},
    }
    return planet_data


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


def draw_planet_icon(planet_name, planet_info, color=True, size=(1.5, 1.5), save_path=None):
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
    orbit_radius = 2.5

    planet_color = {
        'mercury': 'darkgray', 'venus': 'gold', 'earth': 'blue', 'mars': 'red',
        'jupiter': 'orange', 'saturn': 'goldenrod', 'uranus': 'lightblue', 'neptune': 'darkblue'
    }.get(planet_name, 'gray')

    orbit = plt.Circle((0, 0), orbit_radius, fill=False, linestyle='--', edgecolor='gray', lw=0.5)
    ax.add_patch(orbit)

    planet = plt.Circle((0, 0), radius, color=planet_color, ec='black', zorder=2)
    ax.add_patch(planet)

    # This arrow shows the direction of the tilt
    x_tilt = radius * np.sin(angle_rad)
    y_tilt = radius * np.cos(angle_rad)
    arrow = FancyArrowPatch(posA=(0, 0), posB=(x_tilt, y_tilt),
                            arrowstyle='->', color='yellow', lw=2.0,
                            mutation_scale=15)
    ax.add_patch(arrow)

    # This arc shows the size of the tilt angle
    arc_radius = 0.5
    arc_angles = np.linspace(0, angle_rad, num=50)
    arc_x = arc_radius * np.sin(arc_angles)
    arc_y = arc_radius * np.cos(arc_angles)
    ax.plot(arc_x, arc_y, color='black', lw=1.0)

    # This label adds the tilt value on the arc
    label_x = arc_radius * np.sin(angle_rad / 2)
    label_y = arc_radius * np.cos(angle_rad / 2)
    ax.text(label_x, label_y, f"{tilt_angle:.1f}°", fontsize=8, ha='left', va='bottom')

    # Adds the date to the bottom of the image
    timestamp = datetime.now().strftime("Created on %Y-%m-%d")
    ax.text(-2.4, -2.6, timestamp, fontsize=6, ha='left')

    ax.set_title(f"{planet_name.capitalize()}\n{tilt_angle:.1f}°", fontsize=10)

    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.close()

def matrix_demo():
    """
    ___author__ = "Maribel Moreno"
    Builds a 10x10 matrix like in the matrix assignment, solves for eigenvalues and eigenvectors, and prints the results
    """
    matrix_dimension = 10
    n = matrix_dimension

    main_diag = 2 * np.ones(n)
    off_diag = -1 * np.ones(n - 1)

    H = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
    scaling_factor = 1 / (2 * (1 / (n + 1)) ** 2)
    H = scaling_factor * H

    eigenvalues, eigenvectors = np.linalg.eig(H)

    # Sorts them
    i_sorted = np.argsort(eigenvalues)
    eigenvalues = eigenvalues[i_sorted]
    eigenvectors = eigenvectors[:, i_sorted]

    print("\nEigenvalues (lowest to highest):\n", eigenvalues)
    print("\nEigenvectors (each column matches eigenvalue above):\n", eigenvectors)

    return eigenvalues, eigenvectors



def main():
    data = get_data()
    """
    __author__ = "Betzaida Alcaide"
    """
    # Shows tilt stats in the terminal
    stats = compute_tilt_statistics(data)
    print("\nTilt Statistics:", stats)

    # Fit a curve to the tilts
    coeffs, x_vals, y_vals = fit_tilt_curve(data)
    fit_x = np.linspace(0, len(x_vals) - 1, 100)
    fit_y = sum(c * fit_x**i for i, c in enumerate(coeffs))

    # Make the plot with data and fit curve
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

    # Make planet pictures
    for planet, info in data.items():
        draw_planet_icon(planet, info, save_path=f"{planet}_tilt.png")

    # Show matrix answers in the terminal
    eigenvalues, eigenvectors = matrix_demo()
    print("\nEigenvalues:\n", eigenvalues)
    print("\nEigenvectors:\n", eigenvectors)


if __name__ == "__main__":
    main()