import math
listax = [*range(1, 100, 1)]
b = False
simenao = []
contador = 0
todos = []


def geradorfun(x):
    funca = []
    for a in x:
        funca.append(math.cos(a))
    return funca


listay = geradorfun(listax)

for c in listay:
    simenao.append(0)
    if c < 0 and b == False:
        simenao.pop()
        simenao.append(1)
        b = True
    elif c > 0 and b == True:
        simenao.pop()
        simenao.append(1)
        b = False

for d in range(len(simenao)):
    if simenao[d] == 1:
        todos.append(listax[d])

raizes = []

for u in range(0, len(todos), 2):
    primeirovalor = todos[u]
    segundovalor = todos[u+1]
    media = (primeirovalor + segundovalor)/2
    raizes.append(media)
print(listax)
print(listay)
print(raizes)
