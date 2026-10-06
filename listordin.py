#escrever uma sequencia de 5 numeros com espaços

linha = input()

linsptring = linha.split()

listaint = list(map(int, linsptring) )

listainv = listaint[::-1]

for cont in range(len(listainv)):
    print(f"{listainv[cont] }", end=" ")