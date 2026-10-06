#criar um programa que cria um inteiro e mostra todos os divisores

x = int(input())
for divisores in range(1,x+1):
    if x%divisores == 0: 
        print(divisores, end=" ") #end define oq vai ser feito depois do print, seq de caracteres q ele vai imprimir

print() #para nao ficar colado com a msg do terminal