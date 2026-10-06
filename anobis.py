#um ano sera bissexto se ele for divisivel por 400
#OU é divisível por 4 E NÃO é divisível por 100

ano = int(input())

if ano % 400 == 0:
    print("Sim")

elif ano % 4 == 0 or (ano % 100 != 0):
    print("Nao")