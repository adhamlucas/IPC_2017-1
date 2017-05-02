# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# André Luís Laborda Neves           1515070006
# Diego Reis Figueira                1515070169
# João Vitor De Cordeiro B Gonçalves 1515140036
#
#
# 13) Escreva um algoritmo em PORTUGOL que receba dez números do usuário e
#armazene em um vetor o cubo de cada número. Após isso, o algoritmo deve imprimir
# todos os valores armazenados
# ----------------------------------------------------------

list = []
for i in range (0,10):
    numbers = float(input())**3
    list.append(numbers)
print(list)
