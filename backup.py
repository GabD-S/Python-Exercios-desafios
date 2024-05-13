import math

def ondascos(a):
  lt = []
  for i in a:
    o = math.cos(i)
    lt.append(o)
  return lt

def ondassen(a):
  lt = []
  for i in a:
    o = math.sin(i)
    lt.append(o)
  return lt
def ondtg(a):
  lt = []
  for i in a:
    o =math.tan(i)
    lt.append(o)
  return lt

#---------------------
l1l2 = [] #usada
res = []
soma = 0.01
ltx = [] #usada
oscila = True
ini, fim = input().split(',')
ini = round(float(ini),2)
fim = round(float(fim),2)

while ini < fim:
  ltx.append(ini)
  ini = round(ini+soma, 2)
#----------------------

lty = ondascos(ltx)
lty2 = ondassen(ltx)
lty3 = ondtg(ltx)

#with open('cos.txt', 'w') as f:
#    f.write(','.join(str(i) for i in lty))
#with open('sen.txt', 'w') as f:
#    f.write(','.join(str(i) for i in lty2))

#np.savetxt("dados.txt", np.column_stack((ltx, lty, lty2)))

for i in lty3:
    l1l2.append(0)
    
    if i < 0 and not oscila:
        l1l2.pop()
        l1l2.append(1)
        oscila = True
    
    elif i > 0 and oscila:
        l1l2.pop()
        l1l2.append(1)
        oscila = False
    
for d in range(1,len(l1l2)):
  if l1l2[d] == 1:
    a = ltx[d-1]
    b = ltx[d]
    while abs(a-b) > 0.0001: 
      c = (a+b)/2
      if math.cos(a)*math.cos(c) < 0:
        b = c
      else:
        a = c
    res.append(round(c, 2))
    
print(res)


