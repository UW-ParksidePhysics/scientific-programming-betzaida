import vpython as vp


ball_radius = 1


ball_one = vp.sphere(radius=ball_radius)
ball_two = vp.sphere(radius=ball_radius,
                     color=vp.color.blue,
                     pos=vp.vector(*args: 2 * ball_radius, 2*ball_radius, 0)
                     )


ball_two_velocity = vp.vector()