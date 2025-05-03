import numpy as np
import matplotlib.pyplot as plt
import sys


def main():
    # Parse command line arguments
    if len(sys.argv) != 4:
        print("Usage: python3 plot_trajectory.py <y0> <theta_degrees> <v0>")
        return

    y0 = float(sys.argv[1])
    theta_deg = float(sys.argv[2])
    v0 = float(sys.argv[3])

    # Constants
    g = 9.8
    theta = np.radians(theta_deg)

    # X range
    x_values = np.linspace(0, 100, 500)

    # Trajectory formula
    y_values = x_values * np.tan(theta) - ((g * x_values ** 2) / (2 * v0 ** 2 * np.cos(theta) ** 2)) + y0

    # Filter for y ≥ 0
    mask = y_values >= 0
    x_values = x_values[mask]
    y_values = y_values[mask]

    # Plot
    plt.plot(x_values, y_values, label="Projectile trajectory")
    plt.title("Ball Trajectory")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Height (m)")
    plt.grid(True)
    plt.legend()
    plt.savefig("trajectory.png")
    plt.show()


if __name__ == "__main__":
    main()
