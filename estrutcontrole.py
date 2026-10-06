#ESTRUTURAS DE CONTROLE (if, else, elif)

#COMANDO CONDICIONAL SIMPLES: executa só se for verdadeira: permite que a escolha do grupo de ações a ser executado quando determinada condição é satisfeita
#COMANDO CONDICIONAL COMPOSTA: executa uma OU outra

#exemplos: (ESPACINHO É OBRIGATORIOOO)

#if(condição):
    #<blocos de comando> 
#espacinho é chamado de identação, é obrigatório
#indica que o bloco de instruções está dentro do if

idade = 15
if idade >= 18:
     print("Você é maior!")
print("Análise concluída!")

#exemplo:

if(idade >= 18):
     print("Você é maior.")
else:
     if (idade >= 10):
          print("Você tem mais do que 10 anos.")
     else:
         print("Você não tem mais do que 10")