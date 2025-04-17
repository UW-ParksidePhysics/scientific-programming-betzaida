""" My code is going to produce different spin icons based on the planets in the solar system
"""

__author__ = ["Betzaida Alcaide", "Maribel Moreno"]

import numpy as np
import matplotlib.pyplot as plt

def label_icon():
    pass


def draw_planet():
    pass


def draw_poles():
    pass


def draw_orbit():
    pass


def draw_perpendicular_axis():
    pass


def get_data():
    planet_data = {
        'mars': 25.2,
        'earth': 23.44,
        'pluto':
    }
    return planet_data



def test_plot():

    #line
    intercepts = [4, 3]
    x_bounds = np.array([-3, 8])
    x_values = np.linspace(x_bounds[0], x_bounds[1], 100)
    #y_bounds = -intercepts[1] * x_bounds / intercepts[0] + intercepts[1]
    y_values = -intercepts[1] * x_values / intercepts[0] + intercepts[1]

    #circle
    radius = intercepts[0]
    angles = np.linspace( 0, 2 * np.pi, 100)
    circle_xs = radius * np.cos(angles)
    circle_ys = radius * np.sin(angles)
    #plt.plot(x_bounds, y_bounds)
    plt.plot(x_values, y_values)
    plt.plot(circle_xs, circle_ys)
    plt.show()

    return

if __name__ == '__main__':
    data = get_data()
    for planet, tilt in data.items():
        print(f"{planet} = {tilt}°")
    test_plot()













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
