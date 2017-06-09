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
#41.Escreva um algoritmo que gere a série de FIBONACCI até o N-ésimo termo.

serie = int(input("número de termos fibonacci: "))
prim = 1
segu = 0

while serie != 0:

    serie -= 1
    prim += segu
    print (prim)

    if serie != 0:
        serie -= 1
        segu += prim
        print (segu)
