n = int(input())

valores = []

for _ in range(n):
    numero = int(input())

    if numero not in valores:
        valores.append(numero)

    if len(valores) == 25:
        break

for i in range(5):
    for j in range(5):
        print(valores[i * 5 + j], end=" ")
    print()