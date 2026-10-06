matriz = []

for i in range(4):
    linha = []

    for j in range(5):
        numero = int(input())
        linha.append(numero)

    matriz.append(linha)

A = int(input())
B = int(input())

quantidade = 0

for i in range(4):
    for j in range(5):
        if A <= matriz[i][j] <= B:
            quantidade += 1

print(quantidade)