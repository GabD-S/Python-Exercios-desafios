# Variáveis para manter o menor resultado, soma e contador
menor_resultado = None
soma_resultados = 0
contador_resultados = 0

# Loop para as operações
while True:
    # Leitura da operação
    operacao = input().split()
    a = float(operacao[0])
    operador = operacao[1]
    
    # Verificação de término das operações
    if operador == "=":
        break
    
    b = float(operacao[2])
    
    # Verificação se a = b
    if a == b:
        print("*")
        continue
    
    # Execução da operação
    if operador == "+":
        resultado = a + b
    elif operador == "-":
        resultado = a - b
    elif operador == "*":
        resultado = a * b
    elif operador == "/":
        resultado = a / b
    
    # Impressão do resultado
    print("{:.2f}".format(resultado))
    
    # Atualização das variáveis
    if menor_resultado is None or resultado < menor_resultado:
        menor_resultado = resultado
    soma_resultados += resultado
    contador_resultados += 1

# Impressão do menor resultado, soma e média
if menor_resultado is None:
    print("*")
else:
    print("*")
    print("*")
    print("*")
