import numpy as np
import matplotlib.pyplot as plt
from equations_of_state import fit_equation_of_state


def load_volume_energy_data(filepath):
    """
    Loads volume and energy data from a .dat file.

    :param filepath: str, path to the data file
    :return: tuple (volumes, energies)
    """
    data = np.loadtxt(filepath)
    volumes = data[:, 0]
    energies = data[:, 1]
    return volumes, energies


def fit_data_with_murnaghan(volumes, energies):
    """
    Fits the volume-energy data using the Murnaghan equation of state.

    :param volumes: np.ndarray of volume values
    :param energies: np.ndarray of energy values
    :return: tuple of (fit_x, fit_y), and equation parameters
    """
    # Starting guess from quadratic fit
    guess_coeffs = np.polynomial.polynomial.polyfit(volumes, energies, deg=2)

    # Get the fitted y-values and parameters using your instructor's module
    fit_y, eq_params = fit_equation_of_state(
        volumes,
        energies,
        guess_coeffs,
        equation_of_state='murnaghan',
        number_of_points=100
    )

    # Define x-points used
    fit_x = np.linspace(min(volumes), max(volumes), num=100)

    return fit_x, fit_y, eq_params


def plot_equation_of_state(volumes, energies, fit_x, fit_y, save_path):
    """
    Plots volume-energy data and Murnaghan equation fit.

    :param volumes: np.ndarray
    :param energies: np.ndarray
    :param fit_x: np.ndarray
    :param fit_y: np.ndarray
    :param save_path: str, output file name
    """
    plt.figure(figsize=(6, 4))
    plt.scatter(volumes, energies, label='Data', color='black')
    plt.plot(fit_x, fit_y, label='Murnaghan Fit', linestyle='--', color='blue')
    plt.xlabel("Volume ($V$)")
    plt.ylabel("Energy ($E$)")
    plt.title("Alcaide & Moreno – Murnaghan Equation of State")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()


if __name__ == "__main__":
    # Load data
    volumes, energies = load_volume_energy_data("C.Fd-3m.GGA-PBE.volumes_energies.dat")

    # Fit data
    fit_x, fit_y, _ = fit_data_with_murnaghan(volumes, energies)

    # Plot and save
    plot_equation_of_state(
        volumes,
        energies,
        fit_x,
        fit_y,
        save_path="Alcaide_Moreno.C.Fd-3m.GGA.Fm-3m.Murnaghan.EquationOfState.png"
    )
