import vpython as vp

# Wall setup
wall_center = vp.vector(0., 0., 0.)
wall_dimensions = vp.vector(0.25, 10., 10.)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.red)

# Ball properties
radius = 0.5
wall_half_width = wall_dimensions.x / 2

# Ball 1 (starts low, aimed upward angle)
pos1 = vp.vector(-10., -5., 0.)
vel1 = vp.vector(25., 10., 0.)
ball1 = vp.sphere(pos=pos1, radius=radius, color=vp.color.blue, make_trail=True)

# Ball 2 (starts high, aimed downward angle)
pos2 = vp.vector(-10., 5., 0.)
vel2 = vp.vector(25., -10., 0.)
ball2 = vp.sphere(pos=pos2, radius=radius, color=vp.color.green, make_trail=True)

# Time control
animation_time_step = 0.01
rate_of_animation = 1 / animation_time_step
time_step = 0.005
stop_time = 1.0
time = 0.0

while time < stop_time:
    vp.rate(rate_of_animation)

    for ball, vel in [(ball1, vel1), (ball2, vel2)]:
        # Check for collision with wall: x-distance between centers
        if abs(ball.pos.x - wall.pos.x) <= (radius + wall_half_width):
            vel.x = -vel.x  # Bounce: reverse x-direction

        # Update position
        ball.pos += vel * time_step

    time += time_step