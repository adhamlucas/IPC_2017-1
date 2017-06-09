#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Dayana Picanço Marquez            1715310058
# Vitor Simões Azevedo              1715310025
# Wilbert Luís Evangelista Marins   1715310055
# Enrique Leão Barbosa Izel         1715310048
# Edson de Lima Barros              1715310043
# Víctor Hugo de Oliveira Carreira  1715310063
#
#6)Escreva um algoritmo em PORTUGOL que armazene em um vetor todos os números
#múltiplos de 5, no intervalo fechado de 1 a 500. Após isso, o algoritmo deve imprimir
#todos os valores armazenados
#---------------------------------------------------------------------------

numeros = []

for numero in range(1,501):
    if numero % 5 == 0:
        numeros.append(numero)

print(numeros)