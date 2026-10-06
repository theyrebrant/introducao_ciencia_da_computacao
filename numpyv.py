import numpy as np

L = int(input())
C = int(input())

valores = list(map(int, input().split()))

A = np.array(valores).reshape(L, C)

for linha in A:
    print(*linha)

I = int(input())
J = int(input())

print("elemento:", A[I, J])