temperaturas = []

while True:
    temperatura = int(input())
    if temperatura == -999:
        break
    if temperatura < -50 or temperatura > 50:
        print("Erro de leitura")
        continue
    temperaturas.append(temperatura)

if len(temperaturas) == 0:
    print("Nenhuma leitura valida")
else:
    print("Temperaturas:", *temperaturas)
    media = sum(temperaturas) / len(temperaturas)
    print(f"Media: {media:.2f}")