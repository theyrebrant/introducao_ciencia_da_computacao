#escrever um numero arredondado/encurtado
print("O valor é {:.2f}".format(3.14159))

#outro exemplo
nome = "Leandro"
idade = 30
print("Meu nome é %s e tenho %d anos." %(nome, idade))
print("Pi com 3 casas: %.3f" %3.14159)


#outro jeito de escrever
nome = "Anderson"
idade = 20
print(f"Meu nome é {nome} e tenho {idade} anos.")
print(f"Pi com 4 casas: {3.14159: 4f}")
print(f"Idade daqui a 5 anos: {idade + 5}")

#usar a C style para ajudar em estrutura de dados!!

#C style 
nome = "Joel"
idade = 30 
print("Meu nome é %s e tenho %d anos." %(nome, idade))
print("Pi com 3 casas decimais: %.3f" %3.14159)