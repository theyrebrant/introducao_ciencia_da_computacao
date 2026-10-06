A = list(map(int, input().split()))
B = list(map(int, input().split()))

igual = 1

for i in range(5):
    if A[i] != B[i]:
        igual = 0
        break

print(igual)