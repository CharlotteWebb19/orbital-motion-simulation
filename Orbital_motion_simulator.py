"""
Simple 2D orbital motion simulation.

Models a small body orbiting a much larger central mass
using Newtonian gravity and a time-stepping method.

Default parameters approximate the Earth–Sun system.
"""

import numpy as np
import matplotlib.pyplot as plt


# Physical constants
G = 6.67430e-11         # gravitational constant (m^3 kg^-1 s^-2)
M = 1.989e30            # mass of the central body (kg)


# Initial conditions
r = np.array([1.496e11, 0.0], dtype=float)        # position (m)
v = np.array([0.0, 29_780.0], dtype=float)        # velocity (m/s)
dt = 3600      # time step (s)


# Gravitational acceleration
def acceleration(position):
    distance = np.linalg.norm(position)           # distance from centre (m)
    return -G * M * position / distance**3        # acceleration vector (m/s^2)


# Simulation loop
positions = []
num_steps = 9000
for _ in range(num_steps):
    a = acceleration(r)                           # acceleration at current position
    v = v + a * dt                                # update velocity
    r = r + v * dt                                # update position
    positions.append(r.copy())                    # store position for plotting later


# Plot the orbit
positions = np.array(positions)     
x = positions[:, 0]                               # all x values
y = positions[:, 1]                               # all y values
plt.plot(x,y)                                     # plot orbit path
plt.scatter(0, 0, color='red')                    # central mass at origin
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Orbital Motion")
plt.axis("equal")
plt.show()

