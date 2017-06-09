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
#
# A série de FETUCCINE é gerada da seguinte forma: 
# os dois primeiros termos são fornecidos pelo usuário; 
# a partir daí, os termos são gerados com a soma ou 
# subtração dos dois termos anteriores, ou seja:
# A(i) = A(i-1) + A(i-2) para i ímpar
# A(i) = A(i-1) - A(i-2) para i par
# Criar um algoritmo em PORTUGOL que imprima 
# os N primeiros termos da série de FETUCCINE, 
# sabendo-se que para existir esta série serão 
# necessários pelo menos três termos.

termo1 = int(input("primeiro termo: "))
termo2 = int(input("segundo termo: "))
N = int(input("quantidade de termos: "))
c = 2

if N == 1:
    
    print(termo1)
    
else:
    
    if N >= 2:
    
        print(termo1)
        print(termo2)

while c < N:
    
    c += 1
    save = termo2
    
    if c % 2 != 0:
        
        termo2 += termo1
        termo1 = save
        print(termo2)
        
    else:
        
        termo2 -= termo1
        termo1 = save
        print(termo2)
