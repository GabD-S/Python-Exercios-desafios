import math
import matplotlib.pyplot as plt

g = 9.81
L = 1.0
theta0 = math.pi / 4
w0 = 0.0
t_total = 10.0
dt = 0.01

npoints = int(t_total / dt)

theta = [theta0]
w = [w0]
t = [0.0]


for i in range(npoints):
    dtheta_dt = w[i]
    dw_dt = -(g/L) * math.sin(theta[i])

    nvte = theta[i] + dtheta_dt * dt
    angnv = w[i] + dw_dt * dt

    theta.append(nvte)
    w.append(angnv)
    t.append(t[i] + dt)

plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(t, theta, label='Theta (rad)')
plt.xlabel('Time (s)')
plt.ylabel('Theta (rad)')
plt.title('Pendulum Angle Over Time')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, w, label='Angular Velocity (rad/s)', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Pendulum Angular Velocity Over Time')
plt.legend()

plt.tight_layout()
plt.show()
