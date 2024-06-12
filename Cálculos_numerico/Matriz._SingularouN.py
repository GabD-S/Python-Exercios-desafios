import numpy as np
import math
try:
    o1, o2, o3, o4 = input().split(",")
    o1, o2, o3, o4 = float(o1), float(o2), float(o3), float(o4)

    o1 = (o1 * math.pi) / 180
    o2 = (o2 * math.pi) / 180
    o3 = (o3 * math.pi) / 180
    o4 = (o4 * math.pi) / 180

    m1 = 8
    m2 = 7
    g = 9.81

    P_ = [m1 * g, 0, 0, 0, m2 * g, 0]
    P = np.array(P_)

    linha1 = [np.cos(o1), 1, np.cos(o2), 0, 0, 0]
    linha2 = [np.sin(o1), 0, -np.sin(o2), 0, 0, 0]
    linha3 = [0, 0, np.cos(o2), np.cos(o3), 0, -1]
    linha4 = [0, 0, np.sin(o2), -np.sin(o3), 0, 0]
    linha5 = [0, 0, 0, np.cos(o3), np.cos(o4), 0]
    linha6 = [0, 0, 0, np.sin(o3), -np.sin(o4), 0]

    matrizA = np.array([linha1, linha2, linha3, linha4, linha5, linha6])

    resultado = np.linalg.solve(matrizA, P)

    T1 = resultado[0]
    o = resultado[1]
    T2 = resultado[2]
    o2 = resultado[3]
    T3 = resultado[4]
    o3 = resultado[5]
    if T1 < 0 or o < 0 or T2 < 0 or o2 < 0 or T3 < 0 or o3 < 0:
        print("Tá errado")
    else:
        print(f"{T1:.2f}N {o:.2f}N {T2:.2f}N {o2:.2f}N {T3:.2f}N {o3:.2f}N")

    det = np.linalg.det(matrizA)

    if det == 0:
        print("ERRO: o sistema possui infinitas soluções")
    elif det < 1e-10:
        print("ERRO: matriz singular")
    else:
        None
except:
    print("Erro: O sistema possui uma solução única.")
