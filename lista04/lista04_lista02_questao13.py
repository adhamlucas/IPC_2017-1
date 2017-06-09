#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Diogo Roberto Duarte da Costa     1715310056
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro de Mello         1315120052
# Frederico Victor Alfaia Rodrigues 1515200030
# Gabriel Barroso da Silva Lima     1715310011
#
#Criar um programa que receba três valores e indique o maior
#-------------------------------------------------------------------------------------

a = int(input())
b = int(input())
c = int(input())

higher = a
if b > higher:
  higher = b
if c > higher:
  higher = c

print (higher, "eh o maior")
