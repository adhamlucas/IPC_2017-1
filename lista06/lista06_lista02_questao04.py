#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Antônio Diego Furtado da Silva         1715310004
# Aracille de Souza Barbosa              1315120206
# Marcus Vinicius Paes da Silva Santos   1515070060
# Silas Castro de Mendonça               1715310066
# Wesley da Silva Rocha                  1715310026
#
#Escreva um algoritmo em python que armazene em um vetor todos os números
# inteiros de 100 a 200. Após isso, o algoritmo deve imprimir todos os valores
# armazenados.

#---------------------------------------------------------------------------

list = []
count = 0
number = 100
while count < 101:
    if number != 0:
        list.append(number)
        number = number + 1
        count = count + 1
print (list)