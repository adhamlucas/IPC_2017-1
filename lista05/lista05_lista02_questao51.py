#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro De Mello         1315120052
# Silas castro de Mendonça          1715310066
#O valor aproximado do número π pode ser calculado usando-se a série  
# S = 1 - 1/3³ + 1/5³ - 1/7³ + ... 
# Sendo pi = (S*32)^(1/3). Faça um algoritmo em PORTUGOL 
# que calcule e imprima o valor de π usando os 51 primeiros 
# termos da séria acima.

S = 0
c = 0

while c < 52:
    
    if c % 2 == 0:
        S += 1 / (1+(c*2))**3
        
    else:
        S -= 1 / (1+(c*2))**3
        
    c += 1
        
print(S)
