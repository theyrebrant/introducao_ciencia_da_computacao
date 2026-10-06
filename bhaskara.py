import math

a = float(input())
b = float(input())
c = float (input())
delta = b**2 - 4*a*c

if (delta > 0):
    x1 = (-b + math.sqrt(delta)) / 2*a
    x2 = (-b -math.sqrt(delta))/2*a
    print(f"{x1:.1f} {x2:.1f}")
elif(delta == 0):
    x1 = (-b + math.sqrt(delta))/2*a
    print(f"{x1:.1f}")
else:
    print("Nao existem raizes reais")