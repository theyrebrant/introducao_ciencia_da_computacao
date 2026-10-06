matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz.append(linha)

maior = matriz[0][0]
menor = matriz[0][0]

for i in range(5):
    for j in range(5):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz [i][j]

pos_maior = []
pos_menor = []

for i in range(5):
    for j in range(5):
        if matriz[i][j] == maior:
            pos_maior.append((i,j))

for i in range(5):
    for j in range(5):
        if matriz[i][j] == menor:
            pos_menor.append((i,j))

print("MAIOR", maior)
print("QUANTIDADE", len(pos_maior))

for i, j in pos_maior:
    print(i, j)

print("MENOR", menor)
print("QUANTIDADE", len(pos_menor))

for i, j in pos_menor:
    print(i, j)