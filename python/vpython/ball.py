import numpy as np
from vpython import *

# Create a ball (sphere)
ball = sphere(pos=vector(0, 5, 0), radius=0.5, color=color.red)

# Set up the floor
floor = box(pos=vector(0, -0.5, 0), size=vector(10, 0.2, 10), color=color.green)

# Initial velocity
ball.velocity = vector(0, -1, 0)

# Time step for simulation
dt = 0.01

# Animation loop
while True:
    rate(100)  # Control speed of animation
    ball.pos = ball.pos + ball.velocity * dt  # Update position
    if ball.pos.y < 0.5:  # Bounce when hitting the floor
        ball.velocity.y = -ball.velocity.y
    ball.velocity.y += -9.8 * dt  # Apply gravity
