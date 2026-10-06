def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def mdc3(a, b, c):
    return mdc(mdc(a, b), c)


def mmc(a, b):
    return abs(a * b) // mdc(a, b)


def mmc3(a, b, c):
    return mmc(mmc(a, b), c)


a = int(input())
b = int(input())
c = int(input())

print("MDC:", mdc3(a, b, c))
print("MMC:", mmc3(a, b, c))