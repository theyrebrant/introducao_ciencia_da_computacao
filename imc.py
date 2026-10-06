m = float(input())
h = float(input())
imc = m / (h ** 2)

if imc < 18.5:
    situacao = "abaixo do peso"
elif imc < 25:
    situacao = "peso ideal"
elif imc < 30:
    situacao = "acima do peso"
else:
    situacao = "obesidade"

print(f"{imc:.2f}")
print(situacao)