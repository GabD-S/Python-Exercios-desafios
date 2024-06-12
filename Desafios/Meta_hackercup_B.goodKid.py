def func():
    n_fatores = int(input())
    n_mult = list(map(int, input().split()))
    menor = n_mult.index(min(n_mult))
    n_mult[menor] = min(n_mult) + 1
    if n_fatores != len(n_mult):
        print('banido')
    else:
        produto = 1

        for i in n_mult:
            produto = i * produto
        print(produto)


func()
