A = list(map(int, input().split()))

maior = 0

for i in range(1, 10):
    diferenca = abs(A[i] - A[i - 1])

    if diferenca > maior:
        maior = diferenca

print(maior)