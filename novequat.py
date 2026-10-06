matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz.append(linha)

for j in range(5):
    matriz[2][j], matriz[j][2] = matriz[j][2], matriz[2][j]

for i in range(5):
    print(*matriz[i])