from vpython import *
import math

# Constants and initial setup
g_values = {
    "Earth": 9.81,
    "Mars": 3.71,
    "Moon": 1.62
}

colors_fields = {
    "Earth": color.green,
    "Mars": color.red,
    "Moon": color.gray(0.5)
}

colors_balls = {
    "Earth": color.blue,
    "Mars": color.magenta,
    "Moon": color.white
}

field_size = 100
ball_radius = 1
initial_speed = 20
angle_1 = math.pi / 6  # 30 degrees
angle_2 = math.pi / 2 - angle_1  # 60 degrees

# Create fields and balls
fields = {}
balls = {}
labels = {}
positions = {
    "Earth": vector(-field_size, 0, 0),
    "Mars": vector(0, 0, 0),
    "Moon": vector(field_size, 0, 0)
}

for planet in g_values:
    fields[planet] = box(
        pos=positions[planet],
        length=field_size,
        height=0.2,
        width=field_size,
        color=colors_fields[planet]
    )
    balls[planet] = sphere(
        pos=positions[planet],
        radius=ball_radius,
        color=colors_balls[planet],
        make_trail=True
    )
    labels[planet] = label(
        pos=positions[planet] - vector(0, 2, 0),
        text=planet.upper(),
        color=colors_fields[planet],
        box=False
    )

# Function to simulate motion
def simulate_launch(theta):
    dt = 0.01
    velocities = {}

    # Initialize velocities for each planet
    for planet in balls:
        v0 = initial_speed
        vx = v0 * math.cos(theta)
        vy = v0 * math.sin(theta)
        velocities[planet] = vector(vx, vy, 0)

    # Run simulation until Earth ball hits ground
    t = 0
    while balls["Earth"].pos.y >= 0:
        rate(100)
        t += dt
        for planet in balls:
            g = g_values[planet]
            velocity = velocities[planet]
            ball = balls[planet]
            ball.pos += velocity * dt
            velocity.y -= g * dt
            velocities[planet] = velocity

# First launch
simulate_launch(angle_1)

# Reset balls to initial positions
for planet in balls:
    balls[planet].clear_trail()
    balls[planet].pos = positions[planet]

# Second launch
simulate_launch(angle_2)
