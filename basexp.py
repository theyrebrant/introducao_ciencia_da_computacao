base = int(input())
expoente = int(input())

resultado = 1

for i in range(expoente):
    resultado = resultado * base

print(resultado)