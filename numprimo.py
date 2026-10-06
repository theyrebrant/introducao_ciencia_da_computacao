#um número inteiro é considerado primo quando é maior do que 1 e possui exatamente dois divisores positivos distintos: 1 e ele próprio.
#escreva um programa que leia um número inteiro n e informe se ele é primo.
#numeros negativos n sao primos, nem 0 e 1
#sim e nao com primeira letra maiuscula
# usamos 0 pra contagens
#none é algo q nao tem nada na variavel e vai ser atribuido no futuro

n = int(input())
divisores = 1
n_divisores = 0

while divisores <= n:
    if n%divisores == 0:
        n_divisores = n_divisores + 1


    divisores += 1

if n_divisores == 2:
    print("Sim")
else:
    print("Nao")
