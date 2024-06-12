import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def f(x, a):
    return x**(2/3) + np.exp(1)/3 * (np.pi - x**2)**(1/2) * np.sin(a * np.pi * x)


fig, ax = plt.subplots()
ax.set_xlim(0, 3)
ax.set_ylim(-2, 4)

line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,


def animate(a):
    x = np.linspace(0, 3, 1000)
    y = f(x, a)
    line.set_data(x, y)
    return line,


ani = FuncAnimation(fig, animate, frames=np.linspace(0, 2, 100),
                    init_func=init, blit=True)

plt.show()
