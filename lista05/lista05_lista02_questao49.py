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
# Sendo S = 1 + 2/2² + 1/3³ + ... 1/N^n , um somatório de N (definido pelo usuário)
# termos, escreva algoritmo em PORTUGOL para calcular S para um número N.

termos = int(input("quantidade de termos pra soma: "))
c = 2
S = 1

while c <= termos:
    S += 1 / (c ** c)
    c += 1

print ("Resultado:", S)