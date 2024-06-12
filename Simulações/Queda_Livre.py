class quedalivre:
    def __init__(self, s0=0, v0=0, g=10):
      self.s0 = float(s0)
      self.v0 = float(v0)
      self.g = float(g)

    def posicao(self, t):
        t = float(t)
        return self.s0 + self.v0 * t - 0.5 * self.g * t**2

    def velocidade(self, t):
        return self.v0 - self.g * float(t)


posini, t = input().split()
posini = int(posini)
t = int(t)

arquivo = open('result.txt', 'w')

for posini in range(posini, 50, 10):
    for t in range(t, 50, 10):

      queda = quedalivre(posini)

      pos = queda.posicao(t)

      arquivo.write(f'posição em {t} segundos: {pos} m ')
      vel = queda.velocidade(t)
      arquivo.write('----------------------')
      arquivo.write(f'velocidade após {t} segunndos: {vel}')

arquivo.close()
