import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math 

# Entrada de valores
h = st.number_input("Altura da queda (em metros)", value=120.0)
h = float(h)
v0 = st.number_input("Velocidade Inicial (em m/s)", value=0.0)
v0 = float(v0)
g = 9.8
#tmin = st.sidebar.number_input("Tempo mínimo", value=0)
#tmax = st.sidebar.number_input("Tempo máximo", value=10)
#tvals = st.sidebar.slider("Intervalo de tempo", tmin, tmax, (0, 8))

def posicao(t, v0, g):
    s = h + v0 * t - 0.5 * g * t * t
    return s

def velocidade(t, v0, g):  
    v = v0 - g * t
    return v

def update(frame):
    grafico.set_data(t[len(t)//2], pos[:frame])
    ptext.set_text("Posição: {:.2f}".format(pos[frame]))
    ttext.set_text("Tempo: {:.2f}".format(t[frame]))
    return grafico,
    
# calcula o tempo final
tf = (v0 + math.sqrt(2*g*h + v0**2))/g
t = np.linspace(0, tf)

pos = posicao(t, v0, g)
vel = velocidade(t, v0, g)


# Gráfico 1: posição 
fig1, ax1 = plt.subplots()
ax1.plot(t, pos)
ax1.set_title("Queda Livre")
ax1.set_xlabel("Tempo (s)")
ax1.set_ylabel("Posição (m)")
ax1.grid(True)
st.pyplot(fig1)
st.write("Gráfico da Posição x Tempo")

# Gráfico 2: velocidade 
fig2, ax2 = plt.subplots()
ax2.plot(t, vel)
ax2.set_title("Queda Livre")
ax2.set_xlabel("Tempo (s)")
ax2.set_ylabel("Velocidade (m/s)")
ax2.grid(True)
st.pyplot(fig2)
st.write("Gráfico de Velocidade x Tempo")


# Gráfico 3: animação 
fig3, ax3 = plt.subplots()
grafico, = ax3.plot([], [], 'o')
ax3.set_xlim(0, tf)
ax3.set_ylim(0, h + 1.1*v0**2/(2*g))
ax3.set_ylabel("posição (m)")
ttext = ax3.text(0.1, 0.9, '', transform=ax3.transAxes)
ptext = ax3.text(0.1, 0.8, '', transform=ax3.transAxes)

anim = FuncAnimation(fig3, update, frames=len(t), blit=True)

# salva a animação num arquivo html 
with open("myvideo.html", "w") as fname:
  print(anim.to_jshtml(), file=fname)

# abre o arquivo de animação 
with open("myvideo.html", "r") as fname:
    source_code = fname.read() 

# mostra a animação 
components.html(source_code, height = 900, width=900)




# Constants
a = 1.0  # Semi-major axis of Earth's orbit
e = 0.0167
b = math.sqrt(1 - a**2*e**2)  #0.5  # Semi-minor axis of Earth's orbit
theta = np.linspace(0, 2*np.pi, 100)  # Angle values for one orbit


# Function to calculate Earth's position at each frame
def calculate_position(frame):
    x = a * np.cos(theta[frame])
    y = b * np.sin(theta[frame])
    return x, y

# Animation update function
def update2(frame):
    x, y = calculate_position(frame)
    scatter.set_offsets(np.c_[x, y])
    line.set_data(a * np.cos(theta[:frame+1]), b * np.sin(theta[:frame+1]))
    return scatter,

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Create scatter plot for Earth's position
scatter = ax.scatter([], [], color='blue')
sun = ax.scatter([0-e], [0], color='yellow', s=200)
line, = ax.plot([], [], '--', color='red')

# Animation initialization
def init():
    scatter.set_offsets([])
    return scatter,

# Create animation
ani = FuncAnimation(fig, update2, frames=len(theta), blit=True)

# salva a animação num arquivo html 
with open("myvideo2.html", "w") as fname:
  print(ani.to_jshtml(), file=fname)

# abre o arquivo de animação 
with open("myvideo2.html", "r") as fname:
    source_code = fname.read() 

# mostra a animação 
components.html(source_code, height = 900, width=900)




