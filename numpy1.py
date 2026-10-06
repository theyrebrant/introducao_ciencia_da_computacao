import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))

A = A * 2

print(*A)