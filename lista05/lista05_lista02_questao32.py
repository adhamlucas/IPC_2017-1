# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey         1715310059
# Edson de Lima Barros          1715310043
# Enrique Leão Barbosa Izel     1715310048
# Diego Reis figueira           1515070169
# Diogo Roberto Duarte da Costa 1715310056
# Iury da Silva Coelho          1715310069
# Questão 32: Escreva um algoritmo em PORTUGOL que realize a potência de A (número real) por
# B (número inteiro e positivo), ou seja, AB , através de multiplicações sucessivas. Esses
# dois valores são passados pelo usuário através do teclado.
# ----------------------------------------------------------------------------------------------------------------------

po = 1

numberA = float(input("Digite o valor do numero A: "))
numberB = int(input("Digite o valor do numero B: "))

while numberB > 0:
    po *= numberA
    numberB -= 1

print(po)
