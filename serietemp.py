N = int(input())
anterior = int(input())

for posicao in range(2, N + 1):
    atual = int(input())

    if atual <= anterior:
        print(f"Falha na medicao {posicao}")
        break

    anterior = atual
else:
    print("Sequencia crescente")