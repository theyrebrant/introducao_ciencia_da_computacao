#estimar o peso ideal de uma pessoa (tenso)
#se a pessoa for do sexo masculino
#multiplicaar a altura do homem por 72,7 (um float)
#subtrair 58 do resultado
#se a pessoa for do sexo feminino
#multiplicar a altura por 62,1
#subtrair 44,7 do resultado
#escrever a primeira linha com o caractere M ou F
#a segunda linha contem um real A que apresenta altura da pessoa em metros

sexo = input()
altura = float(input())

if sexo == "M":
    peso = 72.7 * altura - 58
else:
    peso = 62.1 * altura - 44.7

print(f"{peso:.2f}")



