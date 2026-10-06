import numpy as np

L = int(input())
C = int(input())

matriz = []

for _ in range(L):
    matriz.append(list(map(float, input().split())))

A = np.array(matriz)

medias = A.mean(axis=0)

print(*[f"{media:.2f}" for media in medias])