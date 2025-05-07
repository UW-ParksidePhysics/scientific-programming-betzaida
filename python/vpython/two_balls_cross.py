import vpython as vp

# Ball 1
pos1 = vp.vector(-2, -1, -2)
vel1 = vp.vector(1, 0.5, 1)
ball1 = vp.sphere(pos=pos1, radius=0.1, color=vp.color.red, make_trail=True)

# Ball 2
pos2 = vp.vector(2, 1, 2)
vel2 = vp.vector(-1, -0.3, -1)
ball2 = vp.sphere(pos=pos2, radius=0.1, color=vp.color.blue, make_trail=True)

# Timing
animation_time_step = 0.1
rate_of_animation = 1 / animation_time_step
time_step = 0.05
stop_time = 10.0

# Animation loop
time = 0.0
while time < stop_time:
    vp.rate(rate_of_animation)

    # Update positions using uniform motion formula: x = x0 + v * t
    ball1.pos = pos1 + vel1 * time
    ball2.pos = pos2 + vel2 * time

    time += time_step