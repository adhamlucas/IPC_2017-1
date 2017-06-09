# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Guilherme Silva de Oliveira       1715310034
# Gabriel Nascimento de Oliveira    1715310052
# Gabriel de Queiroz Souza          1715310044
# Hugo Thadeu Silva Cardoso         1715310013
# Ian Gabriel Costa Machado         1215120276
#
# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos",
# indicando se os valores lidos são múltiplos entre si.
# ----------------------------------------------------------------------------------------------------------------------

A, B = input().split()
A = int(A)
B = int(B)

num1 = A % B
num2 = B % A

if num1 == 0 or num2 == 0:
    print ("Sao Multiplos")
else:
    print ("Nao sao Multiplos")
