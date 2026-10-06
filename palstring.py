string = input()
palavra = input()

palavras = string.split()

contador = 0

for p in palavras:
    if p == palavra:
        contador += 1

print(contador)
