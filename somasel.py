N = int(input())
D = int(input())

soma = 0

for numero in range(1, N + 1):
    if numero % D == 0:
        continue

    soma = soma + numero

print(soma)