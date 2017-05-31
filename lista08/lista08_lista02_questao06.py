#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Fang Yao                           1115180236
# Enrique leão Barbosa Izel          1715310048
# Hugo Thadeu Silva Cardoso          1715310013
# Victor Summer Oliveira             1715310042
# Wilbert Luis Evangelista Marins    1715310055
# Guilherme Silva de Oliveira        1715310034
# Faça um procedimento que recebe 2 vetores A e B de tamanho 10 de inteiros, por parâmetro. Ao final do procedimento B 
#deve conter o fatorial de cada elemento de A. O vetor B deve retornar alterado. 

from lista08.ipc import vetor
a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = input("Digite os valores: ").split()
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
a4 = int(a4)
a5 = int(a5)
a6 = int(a6)
a7 = int(a7)
a8 = int(a8)
a9 = int(a9)
a10 = int(a10)
resut = fat(a1),fat(a2), fat(a3), fat(a4), fat(a5), fat(a6), fat(a7), fat(a8), fat(a9), fat(a10)
b = resut
print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
print(*b)
