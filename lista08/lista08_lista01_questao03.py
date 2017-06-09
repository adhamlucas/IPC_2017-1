#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Natália Cavalcantre Xavier                1715310021
# Diogo Roberto Duarte da Costa             1715310056
# Carlos Eduardo Tapudima de Oliveira	      1715310030
# Walter Nobre                              1715310057
# Dayana Picanço Marquez                    1715310058
#
# 3.Faça um programa com uma função que necessite de três argumontos
# e retorne a soma dos três argumentos.

import ipc.vetor
arg1 = float(input('Digite o valor do primeiro argumento: '))
arg2 = float(input('Digite o valor do segundo argumento: '))
arg3 = float(input('Digite o valor do terceiro argumento: '))
soma = ipc.vetor.somar_tres(arg1,arg2,arg3)

print("A soma é: %d" %soma)