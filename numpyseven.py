import numpy as np

L = int(input())
C = int(input())

matriz1 = []
for _ in range(L):
    matriz1.append(list(map(int, input().split())))

matriz2 = []
for _ in range(L):
    matriz2.append(list(map(int, input().split())))

direcao = input()

A = np.array(matriz1)
B = np.array(matriz2)

if direcao == "V":
    resultado = np.concatenate((A, B), axis=0)
else:
    resultado = np.concatenate((A, B), axis=1)

for linha in resultado:
    print(*linha)