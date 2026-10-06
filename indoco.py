string = input()
palavra = input()

inicio = 0

while True:
    indice = string.find(palavra, inicio)

    if indice == -1:
        break

    print(indice)
    inicio = indice + 1