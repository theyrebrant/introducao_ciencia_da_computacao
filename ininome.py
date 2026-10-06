nome = input()

palavras = nome.split()
iniciais = []

for palavra in palavras:
    iniciais.append(palavra[0])

print(iniciais)