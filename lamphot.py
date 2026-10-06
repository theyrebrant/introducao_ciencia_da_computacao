#hotel com lampadas A e B
#estado inicial delas IA e IB, 0 a lampada
#está apagada e 1 está acesa

#ha tambem interruptores:
#interruptor 1: muda o estado da lampada A (de 0 para 1 ou 1 pra 0)
#interruptor 2: muda o estado de AMBAS lampadas A e B ao mesmo tempo
#dados os estados iniciais (IA, IB) e um estado final desejado
#(FA, FB)
#determinar o numero MINIMO de vezes q os interruptores devem
#ser acionados para atingir a config final

#se IA == FA, nao tenho q alterar
#se IA != FA tenho q alterar
#o mesmo pra IB e FB

IA = int(input())
IB = int(input())
FA = int(input())
FB = int(input())

if IA == FA and IB == FB:
    print(0)
elif IA != FA and IB != FB:
    print(1)
elif IA != FA:
    print(1)
else:
    print(2)