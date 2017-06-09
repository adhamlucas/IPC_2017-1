#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Gabriel Nascimento de Oliveira    1715310052
# Gabriel de Queiroz Souza          1715310044
# Guilherme Silva de Oliveira       1715310034
# Hugo Thadeu Silva Cardoso         1715310013
# Jandinne Duarte de Oliveira       1015070265
# Joelson Pereira Lima              1715310060
#
# 42) A série de RICCI difere da série de FIBONACCI porque os dois primeiros termos são
# fornecidos pelo usuário. Os demais termos são gerados da mesma forma que a série de
# FIBONACCI. Criar um algoritmo em PORTUGOL que imprima os N primeiros
# termos da série de RICCI e a soma dos termos impressos, sabendo-se que para existir
#esta série serão necessários pelo menos três termos. 
#
#----------------------------------------------------------------

contador = 1
ricci = 0
soma = 0
anterior = int(input('escolha o primeiro termo:'))
proximo = int(input('escolha o segundo termo:'))
limite = int(input('escolha a quantidade de  termos:'))

while contador <= limite :
    print(anterior)
    soma = soma + anterior
    ricci = anterior + proximo
    anterior = proximo
    proximo = ricci
    contador = contador + 1

print('a soma dos termos é :',soma)
