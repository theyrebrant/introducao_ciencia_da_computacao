import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))
limite = int(input())

resultado = A[A > limite]

if resultado.size == 0:
    print("Nenhum")
else:
    print(*resultado)