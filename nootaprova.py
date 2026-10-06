n_notas_baixas = 0
n_notas_altas = 0 
soma = 0

nota = float(input())

while nota >= 0:
    if nota < 5:
        n_notas_baixas += 1

    if nota >= 5:
        n_notas_altas += 1

    soma += nota

    nota = float(input())
    
print(f"Baixas: {n_notas_baixas}")
print(f"Altas: {n_notas_altas}")
                                                                
media = soma / (n_notas_baixas + n_notas_altas)

print(f"Media: {media:.2f}")

porcentagem = n_notas_altas / (n_notas_baixas + n_notas_altas) * 100

print(f"Percentual: {porcentagem:.0f}%")

