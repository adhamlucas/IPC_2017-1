#----------------------------------------------------------------
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
#17)A série de Fibonacci é formada pela seqüência:
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
#Escreva um algoritmo em PORTUGOL que armazene em um vetor os 50 primeiros
#termos da série de FIBONACCI. Após isso, o algoritmo deve imprimir todos os
#valores armazenados.
#

anterior = 0
proximo = 1
fibo = 0
c = 1
a = 50
lista = []
while c <= a:
    fibo = anterior + proximo
    anterior = proximo
    proximo = fibo
    lista.append(proximo)
    c = c + 1
print(lista)
print(len(lista))
