#variaveis maior, menor

maior = None
menor = None
nota = float(input())

while nota >= 0:
    if maior is None:
        maior = nota
    elif nota > maior:
        maior = nota
    if menor is None or nota < menor:
        menor = nota

    nota = float(input())

print(maior)
print(menor)
