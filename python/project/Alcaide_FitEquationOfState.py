import numpy as np
import matplotlib.pyplot as plt
from datetime import date

display_graph = True

def parse_file_name(filename):
    parts = filename.split(".")
    chemical_symbol = parts[0]
    crystal_symmetry = parts[1]
    dft_method = parts[2]
    return chemical_symbol, crystal_symmetry, dft_method


def read_two_columns_text(filename):
    data = np.loadtxt(filename)
    return data


def calculate_bivariate_statistics(data):
    x, y = data[:, 0], data[:, 1]
    return {
        "mean_y": np.mean(y),
        "std_y": np.std(y),
        "min_x": np.min(x),
        "max_x": np.max(x),
        "min_y": np.min(y),
        "max_y": np.max(y)
    }


def calculate_quadratic_fit(data):
    x, y = data[:, 0], data[:, 1]
    return np.polynomial.polynomial.polyfit(x, y, deg=2)


def fit_curve_array(coeffs, min_x, max_x, num_points=100):
    x = np.linspace(min_x, max_x, num_points)
    y = coeffs[0] + coeffs[1]*x + coeffs[2]*x**2
    return np.column_stack((x, y))


def convert_units(value, from_units, to_units):
    bohr_to_angstrom = 0.529177
    ryd_to_ev = 13.605693122994
    ryd_per_bohr3_to_gpa = 14710.5

    if from_units == "ryd/bohr^3" and to_units == "GPa":
        return value * ryd_per_bohr3_to_gpa
    elif from_units == "bohr^3" and to_units == "angstrom^3":
        return value * bohr_to_angstrom**3
    elif from_units == "ryd" and to_units == "eV":
        return value * ryd_to_ev
    else:
        raise ValueError(f"Unsupported conversion: {from_units} to {to_units}")


def plot_equation_of_state(data, fit_curve, coeffs, symbol, symmetry, method):
    x_data = data[:, 0]
    y_data = data[:, 1]
    fit_x = fit_curve[:, 0]
    fit_y = fit_curve[:, 1]

    v0 = -coeffs[1] / (2 * coeffs[2])
    e0 = coeffs[0] + coeffs[1]*v0 + coeffs[2]*v0**2
    k0 = 2 * coeffs[2]

    v0_ang3 = convert_units(v0, "bohr^3", "angstrom^3")
    k0_gpa = convert_units(k0, "ryd/bohr^3", "GPa")

    today = date.today().isoformat()

    plt.figure(figsize=(8, 6))
    plt.plot(fit_x, fit_y, 'k--', label="Murnaghan Fit")
    plt.plot(x_data, y_data, 'bo', label="Data")

    plt.axvline(v0, linestyle='--', color='gray')
    plt.text(x_data[0], max(y_data), symbol, fontsize=12)
    plt.text(v0, min(y_data)+0.002, r"$Fd\overline{3}m$", fontsize=14, ha='center')
    plt.text(v0, min(y_data)+0.008, f"$K_0$ = {k0_gpa:.2f} GPa", fontsize=10, ha='center')
    plt.text(v0, min(y_data)+0.014, f"$V_0$ = {v0_ang3:.2f} $\\AA^3$/atom", fontsize=10, ha='center')

    plt.title(f"{symbol} Equation of State ({method}) in DFT")
    plt.xlabel("Volume ($\\AA^3$/atom)")
    plt.ylabel("Energy (eV/atom)")
    plt.text(x_data[0], min(y_data)-0.005, f"Created by Betzaida Alcaide ({today})", fontsize=8)
    plt.legend()
    plt.tight_layout()
    if display_graph:
        plt.show()
    else:
        plt.savefig("Alcaide_Equation_of_State_TestPlot.png", dpi=300)


if __name__ == "__main__":
    filename = "C.Fd-3m.GGA-PBE.volumes_energies.dat"
    symbol, symmetry, method = parse_file_name(filename)

    data = read_two_columns_text(filename)
    coeffs = calculate_quadratic_fit(data)
    stats = calculate_bivariate_statistics(data)
    fit = fit_curve_array(coeffs, stats["min_x"], stats["max_x"])

    plot_equation_of_state(data, fit, coeffs, symbol, symmetry, method)