import numpy as np
import matplotlib.pyplot as plt
import math

azim = [
    -20, -15, -12.5, -10, -5, 0, 5, 10, 12.5, 15, 20,
    -15, -12.5, -10, -5, 0, 5, 10, 12.5, 15,
    -12.5, -10, -5, 0, 5, 10, 12.5,
    -10, -5, 0, 5, 10,
    -5, 0, 5,
    -5, 0, 5,
    0,
    0,
    0
]
azim = [math.radians(r) for r in azim]
zenith = [
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    1, 1, 1, 1, 1, 1, 1, 1, 1,
    1.25, 1.25, 1.25, 1.25, 1.25, 1.25, 1.25,
    1.5, 1.5, 1.5, 1.5, 1.5,
    1.75, 1.75, 1.75,
    2, 2, 2,
    2.5,
    3,
    4,
]

# define binning
rbins = np.linspace(0, 4, 50)
abins = np.linspace(-np.pi, np.pi, 90)

#calculate histogram
hist, _, _ = np.histogram2d(azim, zenith, bins=(abins, rbins))
A, R = np.meshgrid(abins, rbins)


# plot
fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))

pc = ax.pcolormesh(A, R, hist.T, cmap="rainbow", shading='auto')
fig.colorbar(pc)
ax.grid(True)



ax.set_thetamin(-20)
ax.set_thetamax(20)
ax.set_theta_zero_location("N")
ax.set_rorigin(-0.5)

plt.show()