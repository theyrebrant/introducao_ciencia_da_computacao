import numpy as np

inicio = int(input())
fim = int(input())
passo = int(input())

A = np.arange(inicio, fim, passo)

print(*A)
print("soma:", A.sum())