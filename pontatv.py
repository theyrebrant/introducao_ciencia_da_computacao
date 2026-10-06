E = int(input())
A = int(input())
C = int(input())

pontos = 2 * E + 3 * A + 5 * C

if pontos >= 200:
    print("O")
elif pontos >= 150:
    print("S")
elif pontos >= 100:
    print("B")
else:
    print("N")