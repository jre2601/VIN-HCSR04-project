import numpy as np
import matplotlib.pyplot as plt
import math

azim = [10, 15, 0, -10, -12, 0, 0] # Koti morajo biti v radianih
azim = [math.radians(r) for r in azim]
zenith = [1, 2, 3, 4, 2, 3, 0.5]

# define binning
rbins = np.linspace(0, 4, 50)
abins = np.linspace(-np.pi, np.pi, 90)

#calculate histogram
hist, _, _ = np.histogram2d(azim, zenith, bins=(abins, rbins))
A, R = np.meshgrid(abins, rbins)


# plot
fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))

pc = ax.pcolormesh(A, R, hist.T, cmap="rainbow")
fig.colorbar(pc)
ax.grid(True)



ax.set_thetamin(-20)
ax.set_thetamax(20)
ax.set_theta_zero_location("N")
ax.set_rorigin(-0.5)

plt.show()