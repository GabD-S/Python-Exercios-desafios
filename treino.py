import numpy as np
import matplotlib.pyplot as plt

def f(t, y, v, c, k, m):
    return -c*v - k*y/m

def solve_ode(c, k, m, y0, v0, dt, t_final):
    num_steps = int(t_final/dt)
    t = np.zeros(num_steps)
    y = np.zeros(num_steps)
    v = np.zeros(num_steps)

    t[0] = 0
    y[0] = y0
    v[0] = v0

    for i in range(1, num_steps):
        t[i] = t[i-1] + dt
        y[i] = y[i-1] + dt * v[i-1]
        v[i] = v[i-1] + dt * f(t[i-1], y[i-1], v[i-1], c, k, m)

    return t, y, v

# Parâmetros do sistema
k = 2.0  # constante elástica da mola
m = 1.0  # massa do bloco

# Condições iniciais
y0 = 0.0  # deslocamento inicial
v0 = 1.0  # velocidade inicial

# Tempo de simulação
dt = 0.01  # tamanho do passo de integração
t_final = 10.0  # tempo final

# Valores diferentes para o coeficiente de amortecimento c
c_values = [0.5, 1.0, 1.5]

# Resolvendo a equação diferencial e plotando os gráficos
for c in c_values:
    t, y, v = solve_ode(c, k, m, y0, v0, dt, t_final)
    plt.plot(t, y, label='c = {}'.format(c))

plt.xlabel('Tempo')
plt.ylabel('Deslocamento')
plt.legend()
plt.grid(True)
plt.show()
