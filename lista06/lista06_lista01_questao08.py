#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Ulisses Antonio Antonino da Costa 1515090555
# Walter Nobre da Silva conceição 1715310057
# Jandinne Duarte de Oliveira 1015070265
# Vitor Summer Oliveira Pantaleão 1715310042
# Reinaldo vargas 1715310054
#
# 8) Faça um Programa que peça a idade e a altura de 5 pessoas, armazene 
# cada informação no seu respectivo vetor. Imprima a idade e a altura na
# ordem inversa a ordem lida.
#----------------------------------------------------------------------------

age = []
height = []

for i in range (5):
    n = (input("idade: "))
    m = (input("altura: "))
    age.append(n)
    height.append(m)

age.reverse()
height.reverse()

print(age)
print(height)
