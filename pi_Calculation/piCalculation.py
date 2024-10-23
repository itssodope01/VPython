import random
import math

def monte_carlo_pi(num_points):
    inside_circle = 0


    for _ in range(num_points):
        # random (x, y) points in the range [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point lies within the unit circle
        if math.sqrt(x**2 + y**2) <= 1:
            inside_circle += 1

    # ratio of points inside the circle to the total points
    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate


num_points = 1000000
pi_value = monte_carlo_pi(num_points)
print(pi_value)
