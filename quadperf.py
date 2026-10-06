#quadrado perfeito, nao pode usar raiz quadrada sqrt, nem **
#dado um número inteiro positivo N determine todos os números de N a N que são quadrados perfeitos. 
#um número é um quadrado perfeito se sua raiz quadrada for um número inteiro. 

n = int(input())

for divisor in range(1,n + 1):
    if divisor*divisor <= n:
        print(divisor*divisor)