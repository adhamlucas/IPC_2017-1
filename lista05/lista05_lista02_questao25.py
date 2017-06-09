# --------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA - 1515090555
# TIAGO FERREIRA ARANHA - 1715310047
# VÍTOR SIMÕES AZEVEDO - 1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA - 1715310063
# REINALDO VARGAS - 1715310054
#
# Criar um algoritmo em PORTUGOL que leia dez números inteiros e
#  imprima o maior
# e o segundo maior número da lista.
#
# --------------------------------------------------------------------------

cont = 0
maior = 0
maior2 = 0
while cont < 3:
    num = int(input('numero'))
    if num > maior:
        maior2=maior
        maior = num
    cont += 1
print(maior, maior2)
