n = int(input())

if n == 0:
    print("O número é zero.")
elif n < 0:
    print("O número é negativo.")
elif n % 2 == 0 and n > 0:
    print("O número é positivo e par.")
else:
    print("O número é positivo e ímpar.")