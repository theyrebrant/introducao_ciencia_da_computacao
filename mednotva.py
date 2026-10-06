N = int(input())

soma = 0
quantidade = 0

for i in range(N):
    nota = float(input())

    if nota < 0 or nota > 10:
        continue

    soma = soma + nota
    quantidade = quantidade + 1

if quantidade == 0:
    print(0)
    print("0.00")
else:
    media = soma / quantidade
    print(quantidade)
    print(f"{media:.2f}")