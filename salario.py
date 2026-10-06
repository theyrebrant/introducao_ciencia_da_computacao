#programa que calcula um novo salário de um funcionário
#condições:
#se o funcionário receber até 2500 reais ele recebe
#aumento de 20%
#se o funcionario recebe MAIS doq 2500 reais ele
#recebe aumento de 15%

salario = float(input())
bonus = 0 #para evitar erro de inicializar a variavel só na condicional

if salario <= 2500:
    novo_salario = salario * 1.20
else:
    novo_salario = salario * 1.15

print("%.2f" % novo_salario)
