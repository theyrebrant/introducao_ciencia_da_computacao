import numpy as np
L = int(input())
C = int(input())

matriz = []

for _ in range(L):
    matriz.append(list(map(int, input().split())))

A = np.array(matriz)

print("linhas:", A.shape[0])
print("colunas:", A.shape[1])
print("dimensoes:", A.ndim)
print("elementos:", A.size)