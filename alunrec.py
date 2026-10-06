freq = float(input())
notap1 = float(input())
notap2 = float(input())
trabalho = float(input())

MS = 0.4 * notap1 + 0.4 * notap2 +0.2 * trabalho

if MS >= 5 and freq >= 0.7:
    MF = MS
    print(f"Aprovado com média final {MF}")
elif MS >= 3 and freq >= 0.7:
    MR = float(input())
    if MR > (10 - MS):
        MF = (MS + MR)/2
    elif 5 <= MR <= (10 - MS):
        MF = 5.0
    else:
        MF = MS
    if MF >= 5:
        print(f"Aprovado com média final {MF}")
    else:
        print(f"Reprovado com média final {MF}")
else:
    MF = MS
    print(f"Reprovado com média final {MF}")