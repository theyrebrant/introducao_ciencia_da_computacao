n = int(input())

matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input()))
    matriz.append(linha)

# Usamos a soma da primeira linha como referência
soma_magica = sum(matriz[0])

magico = True

# Verificar linhas
for i in range(n):
    if sum(matriz[i]) != soma_magica:
        magico = False

# Verificar colunas
for j in range(n):
    soma = 0

    for i in range(n):
        soma += matriz[i][j]

    if soma != soma_magica:
        magico = False

# Verificar diagonais
soma_principal = 0
soma_secundaria = 0

for i in range(n):
    soma_principal += matriz[i][i]
    soma_secundaria += matriz[i][n - 1 - i]

if soma_principal != soma_magica:
    magico = False

if soma_secundaria != soma_magica:
    magico = False

if magico:
    print("SIM")
else:
    print("NAO")