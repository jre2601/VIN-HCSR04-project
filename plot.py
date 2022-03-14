import numpy as np
import matplotlib.pyplot as plt
import math

azim = [
    *[i for _ in range(5) for i in [-20, -15, -12.5, -10, -5, 0, 5, 10, 12.5, 15, 20]]*5,
    *[i for _ in range(4) for i in [-15, -12.5, -10, -5, 0, 5, 10, 12.5, 15]]*5,
    *[i for _ in range(4) for i in [-12.5, -10, -5, 0, 5, 10, 12.5]]*4,
    *[i for _ in range(3) for i in [-10, -5, 0, 5, 10]]*3,
    *[i for _ in range(4) for i in [-5, 0, 5]]*3,
    *[i for _ in range(3) for i in [-5, 0, 5]],
    *[i for _ in range(15) for i in [0]]
]
print(azim.__len__())
azim = [math.radians(r) for r in azim]
zenith = [
    *[round(i, 1) for i in np.arange(0.1, 0.6, 0.1) for _ in range(11)]*5,
    *[round(i, 1) for i in np.arange(0.6, 1.0, 0.1) for _ in range(9)]*5,
    *[round(i, 1) for i in np.arange(1.0, 1.3, 0.1) for _ in range(7)]*4,
    *[round(i, 1) for i in np.arange(1.4, 1.6, 0.1) for _ in range(5)]*3,
    *[round(i, 1) for i in np.arange(1.7, 2.0, 0.1) for _ in range(3)]*3,
    *[round(i, 1) for i in np.arange(2.2, 2.5, 0.1) for _ in range(3)],
    *[round(i, 1) for i in np.arange(2.5, 4, 0.1)]
]
print(zenith.__len__())

# define binning
rbins = np.linspace(0, 4, 39)
abins = np.linspace(-np.pi, np.pi, 90)

#calculate histogram
hist, _, _ = np.histogram2d(azim, zenith, bins=(abins, rbins), normed=True)
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
# fig.savefig('Meritve_high_res.svg', format='svg', dpi=1200)
plt.show()