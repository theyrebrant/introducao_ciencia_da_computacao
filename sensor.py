N = int(input())
quantidade = 0
soma = 0

for i in range(N):
    leitura = int(input())

    if leitura == -1:
        break

    if leitura < 0 or leitura > 100:
        continue

    quantidade = quantidade + 1
    soma = soma + leitura

print(quantidade)
print(soma)