n1 = int(input())
n2 = int(input())
operacao = input()

if operacao == "+":
    resultado = n1 + n2
    print(resultado)
elif operacao == "-":
    resultado = n1 - n2
    print(resultado)
elif operacao == "*":
    resultado = n1 * n2
    print(resultado)
elif operacao == "/":
    if n2 == 0:
        print("Erro: divisao por zero")
    else:
        resultado = n1 / n2
        print(f"{resultado:.2f}")
        
else:
    print("Erro: operacao invalida")