S = int(input())
T = int(input())

acertou = False

for tentativa in range(1, T + 1):
    codigo = int(input())

    if codigo == S:
        print(f"Acertou na tentativa {tentativa}")
        acertou = True
        break

if not acertou:
    print("Acesso bloqueado")