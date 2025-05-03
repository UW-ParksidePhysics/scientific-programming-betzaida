"""
make_hertzsprung_russell_diagram
================================
Generate the Hertzsprung-Russell diagram as depicted in this image:
    https://en.wikipedia.org/wiki/Hertzsprung%E2%80%93Russell_diagram#/media/File:HRDiagram.png
"""

import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

astronomical_unit = 1.495978707e11  # meters
meters_to_light_years = 1. / 9.4607e15


def star_colormap(star_b_minus_vs):
    number_of_gradient_points = 256
    white_index = int((0.33 / (0.33 + 1.40)) * number_of_gradient_points)
    yellow_index = int(((0.81 + .33) / (0.33 + 1.40)) * number_of_gradient_points)
    color_values = np.ones((number_of_gradient_points, 4))

    # Red
    color_values[:white_index, 0] = np.linspace(112 / 255, 255 / 255, white_index)
    color_values[white_index:yellow_index, 0] = 1
    color_values[yellow_index:, 0] = 1

    # Green
    color_values[:white_index, 1] = np.linspace(112 / 255, 255 / 255, white_index)
    color_values[white_index:yellow_index, 1] = 1
    color_values[yellow_index:, 1] = np.linspace(255 / 255, 127 / 255, number_of_gradient_points - yellow_index)

    # Blue
    color_values[:white_index, 2] = 1
    color_values[white_index:yellow_index, 2] = np.linspace(255 / 255, 127 / 255, yellow_index - white_index)
    color_values[yellow_index:, 2] = 127 / 255

    new_colormap = ListedColormap(color_values)

    # Normalize B-V values between 0 and 1
    scaled_b_minus_vs = (star_b_minus_vs - np.min(star_b_minus_vs)) / (np.max(star_b_minus_vs) - np.min(star_b_minus_vs))

    return scaled_b_minus_vs, new_colormap


def parallax_to_distance(parallax):
    parallax_in_radians = (parallax / 1000. / 3600.) * (2 * np.pi / 360.)
    return astronomical_unit / np.tan(parallax_in_radians)


def apparent_to_absolute_magnitude(apparent_magnitude, distance):
    distance_in_parsecs = distance / (648000. * astronomical_unit / np.pi)
    return apparent_magnitude - 5 * np.log10(distance_in_parsecs) + 5


def read_file(filename):
    hipparcos_data = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            parts = line.split()
            if len(parts) < 4:
                continue
            catalog_id = parts[0]
            parallax = float(parts[1])
            app_mag = float(parts[2])
            bv = float(parts[3])
            hipparcos_data[catalog_id] = {
                'parallax': parallax,
                'apparent_magnitude': app_mag,
                'blue_minus_visual': bv
            }
    return hipparcos_data


if __name__ == '__main__':
    hipparcos_dictionary = read_file('hipparcos_data.txt')

    star_absolute_magnitudes = []
    star_b_minus_vs = []

    for star in hipparcos_dictionary.values():
        try:
            distance = parallax_to_distance(star['parallax'])
            abs_mag = apparent_to_absolute_magnitude(star['apparent_magnitude'], distance)
            bv = star['blue_minus_visual']
            if -0.5 <= bv <= 2.0:
                star_absolute_magnitudes.append(abs_mag)
                star_b_minus_vs.append(bv)
        except:
            continue

    star_absolute_magnitudes = np.array(star_absolute_magnitudes)
    star_b_minus_vs = np.array(star_b_minus_vs)

    plt.style.use('dark_background')

    # Invert magnitude axis
    star_absolute_magnitudes = -star_absolute_magnitudes

    # Color mapping
    scaled_bv, cmap = star_colormap(star_b_minus_vs)

    # Plotting
    plt.figure(figsize=(10, 12))
    plt.scatter(star_b_minus_vs, star_absolute_magnitudes, c=scaled_bv, cmap=cmap, s=1, alpha=0.7)

    plt.xlabel("B-V Color Index")
    plt.ylabel("Absolute Magnitude")
    plt.title("Hertzsprung-Russell Diagram")
    plt.gca().invert_yaxis()

    # Label your name below the axis
    plt.text(min(star_b_minus_vs), min(star_absolute_magnitudes) - 1, "Created by Maribel Moreno", fontsize=8)

    # Match the look of the HR diagram
    plt.xlim(-0.5, 2.0)
    plt.ylim(min(star_absolute_magnitudes) - 1, max(star_absolute_magnitudes) + 1)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("hertzsprung_russell_diagram.png")
    plt.show()