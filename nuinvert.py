#dado um N positivo de 3 DIGITOS, ele quer q eu
#construa outro N a partir dele utilizando os mesmos digitos 
#na ordem inversa
#a entrada deve conter uma unica linha com N positivo
#a saída será a mesma coisa, soq na ordem inversa
#a inversão não pode produzir zeros à esquerda

N = int(input())
#a lógica aqui é usar o resto da divisão para
#fazer o número na ordem inversa

primeiro = N // 100
ultimo = N % 10
#para achar o numero do meio ficamos com
meio = N // 10 % 10

inversao = ultimo * 100 + meio * 10 + primeiro

print(inversao)
