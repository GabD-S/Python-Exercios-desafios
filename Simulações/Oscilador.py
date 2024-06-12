import math 
import numpy as np 
import itertools

def ondascos(a):
    return[math.cos(i) for i in a]
def ondasen(a):
    return [math.sin(i) for i in a]
def ondtg(a):
    return [math.tan(i) for i in a]

soma = 0.01
ini,fim = map(float,input().split(','))
ltx = np.arange(ini,fim,soma)

lty  = ondascos(ltx)
lty2 = ondasen(ltx)
lty3 = ondtg(ltx)

l1l2 = np.where(np.diff(np.sign(lty)) != 0,1,0).tolist()

res = []
for d, val in enumerate(l1l2[1:], start=1):
    if val == 1:
        a,b = ltx[d-1], ltx[d]
        while abs(a-b) > 0.00001:
            c=(a+b)/2
            a,b = (a,c) if math.cos(a)*math.cos(c) < 0 else(c,b)
        res.append(round(c,4))
res = list(map(lambda x: float(x)*2, res))
print(res)
