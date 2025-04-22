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

# Global visualization settings
FIG_SIZES = [(1.5, 1.5), (3, 3)]
COLOR_MODES = [True, False]  # True = color, False = black & white

# PLANETARY FUNCTIONS

def label_icon(ax, planet_name, tilt_angle):
    """
    Author: Maribel Moreno
    Adds label to the plot showing the planet name and tilt.
    """
    ax.set_title(f"{planet_name.capitalize()}\n{tilt_angle:.1f}°", fontsize=10)

def draw_planet(ax, radius=1.0, color='gray'):
    """
    Author: Betzaida Alcaide
    Draws a circle representing the planet.
    """
    circle = plt.Circle((0, 0), radius, color=color, ec='black', zorder=2)
    ax.add_patch(circle)

def draw_poles(ax, tilt_angle_deg, radius=1.0, color='black'):
    """
    Author: Betzaida Alcaide
    Draws a line indicating the tilted pole axis.
    """
    angle_rad = np.radians(tilt_angle_deg)
    x = radius * np.sin(angle_rad)
    y = radius * np.cos(angle_rad)
    ax.plot([0, x], [0, y], color=color, lw=2.0, zorder=3)

def draw_orbit(ax, orbit_radius=2.5):
    """
    Author: Betzaida Alcaide
    Draws a dashed orbit circle around the planet.
    """
    orbit = plt.Circle((0, 0), orbit_radius, fill=False, linestyle='--', edgecolor='gray', lw=0.8)
    ax.add_patch(orbit)

def draw_perpendicular_axis(ax, radius=1.5, color='black'):
    """
    Author: Betzaida Alcaide
    Draws a vertical dashed line from which tilt is measured.
    """
    ax.plot([0, 0], [-radius, radius], linestyle='--', color=color, lw=1.0)

def get_data():
    """
    Author: Betzaida Alcaide
    This function returns the tilt angles of the planets.
    """
    planet_data = {
        'mars': 25.2,
        'earth': 23.44,
        'pluto': 122.5
    }
    return planet_data

# TEST FUNCTION

def test_plot():
    """
    Author: Maribel Moreno
    Function to test basic visuals for a planet with tilt and orbit.
    """
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.set_aspect('equal')
    ax.axis('off')

    planet_name = 'earth'
    tilt = 23.44
    color = 'blue'

    draw_orbit(ax)
    draw_planet(ax, color=color)
    draw_perpendicular_axis(ax)
    draw_poles(ax, tilt, color='orange')
    label_icon(ax, planet_name, tilt)

    plt.show()

# MAIN EXECUTION BLOCK

if __name__ == '__main__':
    data = get_data()
    for planet, tilt in data.items():
        print(f"{planet} = {tilt}°")
    test_plot()



# def label_icon(ax, tilt_deg, planet_name):
#    """
#    Author: Maribel moreno
#    This will label the icon with the planet's name and its tilt angle
#    """
    #Formats the label text
#    label = f"{planet_name.title()}: {tilt_deg:.1f}°"

    #Places the label
#    ax.text(0.5, 1.4, label,
#            ha='center', va='center',
#            fontsize=10, fontweight='bold',)


# def draw_planet():
#    """
#    Author: Maribel Moreno
#    This draws the orbit, perpendicular axis, axial tilt, and label for each planet defined in gen_data()
#    """
#    data = get_data()
#
#    for planet, tilt in data.items():
#        fig, ax = plt.subplots(figsize=(3, 3))

        # Draw components
#        draw_orbit(ax)
#        draw_perpendicular_axis(ax)
#        draw_poles(ax, tilt)
#        label_icon(ax, tilt, planet)

        # Plot styling
#        ax.set_aspect('equal')
#        ax.set_xlim(-2, 2)
#        ax.set_ylim(-2, 2)
#        ax.axis('off')     # removes axes for clear icon
#        plt.title(f"{planet.title()} Spin Icon", fontsize=12)

        # Show or save
#        plt.show()


# def draw_poles(ax, tilt_deg, length=1.5):
#    """
#    Author: Maribel Moreno
#    This will draw the axial tilt of the planet from the center
#    """
    # Converts angle to radians
#    tilt_rad = np.radians(tilt_deg)

    # Computes line endpoints using trig
#    x = np.array([-length * np.sin(tilt_rad), length * np.sin(tilt_rad)])
#    y = np.array([-length * np.cos(tilt_rad), length * np.cos(tilt_rad)])

    #Plots the tilted axis
#    ax.plot(x, y, 'r--', linewidth=2, label=f'Tilt = {tilt_deg:.1f}°')


# def draw_orbit(ax, radius=1.0):
#    """
#    Author: Betzaida Alcaide
#    This will draw the planets orbital plane of the planet
#    """
    # Creates angle values from 0 to 2*pi
#    theta = np.linspace(0, 2 * np.pi, 100)

    # Parametric equations for a circle (x = r*cos, y = r*sin)
#    x = radius * np.cos(theta)
#    y = radius * np.sin(theta)

    #Plots the orbit line
#    ax.plot(x, y, 'k', label='Orbital Plane')


# def draw_perpendicular_axis(ax, length=1.5):
#    """
#    Author: Betzaida Alcaide
#     This will draw a perpendicular axis of the planet from the center perpendicular to the orbit
#    """
    #The line that goes from -length to +length vertically
#    x = [0, 0]
#    y = [-length, length]

#    ax.plot(x, y, 'b', linewidth=2, label='Perpendicular Axis')

# def get_data():
#    """
#    Author: Betzaida Alcaide
#    This will show the tilt angle of the 3 planets
#    """
#    planet_data = {
#        'mars': 25.2,
#        'earth': 23.44,
#        'pluto': 122.5
#    }

#    return planet_data



# def test_plot():

    #line
#    intercepts = [4, 3]
#    x_bounds = np.array([-3, 8])
#    x_values = np.linspace(x_bounds[0], x_bounds[1], 100)
#    #y_bounds = -intercepts[1] * x_bounds / intercepts[0] + intercepts[1]
#    y_values = -intercepts[1] * x_values / intercepts[0] + intercepts[1]

    #circle
#    radius = intercepts[0]
#    angles = np.linspace( 0, 2 * np.pi, 100)
#    circle_xs = radius * np.cos(angles)
#    circle_ys = radius * np.sin(angles)
#    #plt.plot(x_bounds, y_bounds)
#    plt.plot(x_values, y_values)
#    plt.plot(circle_xs, circle_ys)
#    plt.show()

#    return

# if __name__ == '__main__':
#   draw_planet()


    # data = get_data()
   # for planet, tilt in data.items():
   #     print(f"{planet} = {tilt}°")
   # test_plot()













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
