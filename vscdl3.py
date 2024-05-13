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
