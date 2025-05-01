""" My code is going to produce different spin icons based on the planets in the solar system
feedback:
-make a 1.5x 1.5 in version and a 3 x 3 in version
-make a black and white version and color version
-dont include the rotational period
-indicate the planets orbit and the perpendicular from which the planetary tilt is measured
-indicate the rotational direction using a curved arrow around the equator
-mark the arc of swept out angle between perp the orbit and the pole, and label the angle there
-include digits to the tenth of the degree (ex: 23.4 degree sign){option, shift, 8 = degree)

"""

__author__ = ["Betzaida Alcaide", "Maribel Moreno"]

import numpy as np
import matplotlib.pyplot as plt

# Extended planetary data including orbit and angular velocity
planet_data = {
    'mars': {'tilt': 25.2, 'a': 227.9e6, 'b': 227.9e6, 'omega': 360 / 24.6},
    'earth': {'tilt': 23.4, 'a': 149.6e6, 'b': 149.6e6, 'omega': 360 / 24.0},
    'pluto': {'tilt': 122.5, 'a': 5906.4e6, 'b': 5906.4e6, 'omega': 360 / 153.0},
}


def get_data():
    return planet_data


def draw_planet_icon(planet_name, planet_info, color=True, size=(3, 3), save_path=None, time=0):
    fig, ax = plt.subplots(figsize=size)
    ax.set_aspect('equal')
    ax.axis('off')

    # Unpack parameters
    tilt_angle = planet_info['tilt'] + planet_info['omega'] * time
    angle_rad = np.radians(tilt_angle)
    radius = 1.0
    orbit_radius = 2.5

    # Colors
    planet_color = 'gray' if not color else {'earth': 'blue', 'mars': 'red', 'pluto': 'brown'}.get(planet_name, 'gray')

    # Draw orbit ellipse
    orbit = plt.Circle((0, 0), orbit_radius, fill=False, color='gray', linestyle='--', lw=0.5)
    ax.add_patch(orbit)

    # Draw planet
    circle = plt.Circle((0, 0), radius, color=planet_color, ec='black', zorder=2)
    ax.add_patch(circle)

    # Equator
    ax.plot([-radius, radius], [0, 0], color='black', lw=1.2, zorder=3)

    # Perpendicular axis (from orbit)
    ax.plot([0, 0], [-1.5 * radius, 1.5 * radius], color='black', lw=1.0, linestyle='--', zorder=1)

    # Tilt axis
    x_tilt = radius * np.sin(angle_rad)
    y_tilt = radius * np.cos(angle_rad)
    ax.plot([0, x_tilt], [0, y_tilt], color='yellow' if color else 'black', lw=2.0, zorder=4)

    # Arc for tilt angle
    arc_radius = 0.5
    arc_angles = np.linspace(0, angle_rad, 50)
    arc_x = arc_radius * np.sin(arc_angles)
    arc_y = arc_radius * np.cos(arc_angles)
    ax.plot(arc_x, arc_y, color='black', lw=1.0)

    # Angle label
    label_x = arc_radius * np.sin(angle_rad / 2)
    label_y = arc_radius * np.cos(angle_rad / 2)
    ax.text(label_x, label_y, f"{tilt_angle:.1f}°", fontsize=8, ha='left', va='bottom')

    # Rotation arrow along equator (semicircular above planet)
    theta = np.linspace(-np.pi / 2, np.pi / 2, 100)
    r = radius
    arrow_x = r * np.cos(theta)
    arrow_y = 0.15 * radius * np.sin(theta)  # slight vertical offset to appear above the equator
    ax.plot(arrow_x, arrow_y, color='black', lw=1.0)
    ax.annotate('', xy=(arrow_x[-1], arrow_y[-1]), xytext=(arrow_x[-2], arrow_y[-2]),
                arrowprops=dict(arrowstyle="->", lw=1.0))

    # Label
    ax.set_title(planet_name.capitalize(), fontsize=10)

    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.close()


def run_all():
    data = get_data()
    for planet, info in data.items():
        for size in [(3, 3), (1.5, 1.5)]:
            draw_planet_icon(planet, info, color=True, size=size, save_path=f"{planet}_color_{size[0]}x{size[1]}.png")
            draw_planet_icon(planet, info, color=False, size=size, save_path=f"{planet}_bw_{size[0]}x{size[1]}.png")


if __name__ == '__main__':
    run_all()





#### RENAME from spin_icons.py to (your_project_short_name).py
# File structure
# 1. Commented paragraph describing project ~ 100-200 words
# 2. Module imports that are used in multiple functions
# 3. Function definitions
# 4. if __name__ == "__main__" block, which calls a primary function with a clear name 

# All code is inside function definitions for simulation solution & visualization (functional programming)
#	Each function contains a docstring compliant with PEP 257: https://www.python.org/dev/peps/pep-0257/
#	Module ends with if __name__ == "__main__" block to execute central function of the code

# Primary simulation function structure
#	1. Module imports
#		Use SciPy constants for physical constants in particular function (not globally)
#			https://docs.scipy.org/doc/scipy/reference/constants.html
#		Follow best practice order: 
#			https://docs.python.org/3/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module
# 	2. Simulation parameters
#		Each parameter named clearly and units marked in in-line comment
#		Naming of all variables should comply with PEP 8: 
#			https://www.python.org/dev/peps/pep-0008/#documentation-strings
#			(lower_case_with_underscores)
# 	3. Computed parameters (from simulation parameters)
# 	4. Function calls (use PEP 8-compliant lower_case_with_underscores) and simple calculations for:
#		data read-in
#		simulation solution 
#		visualization
