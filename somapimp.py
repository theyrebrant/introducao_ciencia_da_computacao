numeros = list(map(int, input().split()))

soma = 0

for i in range(1, 10, 2):
    soma = soma + numeros[i]

print(soma)