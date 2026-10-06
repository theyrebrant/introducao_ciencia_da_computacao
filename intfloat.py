#exercico que le um numero decimal, separa a parte inteira da decimal
#e depois exibe no formato <inteiro> + <decimal>
#tenho q mostrar a parte inteira como int e a parte decimal como float
#importante: formatar o float para ter duas casas decimais depois da virgula com f-string


valor = float(input())
#como quero a parte inteira, temos de usar / / para obter a
#parte inteira de uma divisão (tipo 12.4 / / 1, nesse 
#caso o valor dado será 12. ou seja, nesse caso o
#exercício me pede para printar um inteiro na resposta)
inteiro = int(valor // 1) #isso porque o inteiro irá pegar o meu valor e tirar um inteiro dele
#quando eu quiser obter o resto da divisão irei usar % 
# nesse caso, 15%4 me retornaria 3
decimal = valor % 1

print(f"{inteiro} + {decimal:.2f}")

