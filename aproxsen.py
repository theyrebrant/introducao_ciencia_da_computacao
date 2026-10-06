x = float(input())
n = int(input())

termo = x
resultado = x

for k in range(1, n):
    termo = -termo * x * x / ((2 * k) * (2 * k + 1))
    resultado = resultado + termo

print(f"{resultado:.6f}")