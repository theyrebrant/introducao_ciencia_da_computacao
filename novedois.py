matriz = []

for i in range(4):
    linha = []

    for j in range(5):
        numero = int(input())
        linha.append(numero)

    matriz.append(linha)

somas = []

for j in range(5):
    soma = 0

    for i in range(4):
        soma += matriz[i][j]

    somas.append(soma)

print(*somas)