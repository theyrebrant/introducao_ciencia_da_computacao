def eh_primo(n):
    if n < 2:
        return 0

    for i in range(2, n):
        if n % i == 0:
            return 0

    return 1


n = int(input())

for i in range(2, n + 1):
    if eh_primo(i) == 1:
        print(i)