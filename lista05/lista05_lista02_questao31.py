#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058

# 31- Escreva um algoritmo em PORTUGOL que realize o produto de A (número real) por
# B (número inteiro), ou seja, A * B, através de adições (somas). Esses dois valores são
# passados pelo usuário através do teclado.

a = float(input(' Digite o número A: '))
b = int(input(' Digite o número B: '))
count = 1
mult= 0

while ( count <= b ):

    mult += a
    count += 1

print(' A * B = ', "%.2f" % mult)