#---------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# André Luis Laborda                  1515070006
# Judá Salazar Braga                  1515200050
# Luiz Daniel Raposo Nunes de Mello   1715310049
# Luiz Paulo Machado                  1515200542
# Lukas Michel Souza Mota             1715310018
# 
# Faça um procedimento que recebe 2 vetores A e B de tamanho 10 de
# inteiros, por parâmetro. O procedimento deve retornar um vetor C,
# por parâmetro, que contém os elementos de A e B em ordem decrescente
#---------------------------------------------------------------------

from ipc import vetor

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = vetor.junta_e_ordena(a, b)
print(c)
