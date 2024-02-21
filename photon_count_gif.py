import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

photon_number = 100
size = 17
x = np.arange(-(size + 1) / 2, (size + 1) / 2 + 0.01, 0.01)
tick = int((((size + 1) / 2)-(-(size - 1) / 2))//0.5)
print(tick)
sigma = 2.5
gaussian = np.exp(-x**2 / (2 * sigma**2)) / (np.sqrt(2 * np.pi) * sigma)
gaussian = gaussian / sum(gaussian)

gaus_dis = [random.choices(x, gaussian) for i in range(1, photon_number + 1)]
gaus_dis = [item for sublist in gaus_dis for item in sublist]

fig, ax = plt.subplots()
ax.set_xlim(min(x),-min(x))
ax.set_ylim(0, max(plt.hist(gaus_dis, bins=tick, range=(min(gaus_dis), max(gaus_dis)))[0]))

ax.set_title('Photon Distribution')
ax.set_xlabel('Value')
ax.set_ylabel('Photon Count')
ax.grid(True)
lines, = ax.plot([], [])
def init():
    lines.set_data([], [])
    return lines,

def update(n_terms):
    photon_dis = gaus_dis[:n_terms]
    ax.clear()
    ax.set_xlim(min(x),-min(x))
    ax.set_ylim(0, max(plt.hist(photon_dis, bins=tick, range=(min(gaus_dis), max(gaus_dis)))[0]))
    ax.set_title(f'Photon Distribution (n={n_terms})')
    return lines,

max_terms = photon_number

ani = FuncAnimation(fig, update, frames=max_terms + 1, init_func=init, repeat=False, blit=True)
ani.save('photon_dis.gif', writer='ffmpeg', fps=15)
