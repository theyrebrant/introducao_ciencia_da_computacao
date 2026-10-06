idade = int(input())
renda = float(input())
compras_ano = float(input())
tempo_cadastro = int(input())
pontsatis = int(input())

if idade < 0 or renda < 0 or compras_ano < 0 or tempo_cadastro < 0 or pontsatis < 0 or pontsatis > 100:
    print("Erro: dados de entrada invalidos")

elif pontsatis >= 90 and compras_ano >= 20000:
    print("VIP")

elif renda >= 10000 or (compras_ano > 10000 and tempo_cadastro >= 3):
    print("Alto Potencial")

elif 25 <= idade <= 60 and pontsatis >= 50:
    print("Regular")

else:
    print("Baixa Prioridade")