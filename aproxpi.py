n = int(input())

soma = 0

for i in range(n):
    termo = 4 / (2 * i + 1)

    if i % 2 == 0:
        soma = soma + termo
    else:
        soma = soma - termo

print(f"{soma:.6f}")