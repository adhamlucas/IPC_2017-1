# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# GRUPO 9
# Fang Yao                         1115180236
# Antonio Diego Furtado da Silva   1715310004
#
# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
#
#----------------------------------------------------------------

TermoN = int(input("Informe valor inteiro: "))

Resultado = 1

cont = 2

while cont <= TermoN:
    Resultado = Resultado + 1/(cont)
    cont += 1

print("Resultado: ", Resultado)
