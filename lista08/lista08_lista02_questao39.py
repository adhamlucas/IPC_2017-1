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
# Faça uma função que receba, por parâmetro, uma matriz A(12, 12) e
# retorne a média aritmética dos elementos abaixo da diagonal
# principal
# 
#---------------------------------------------------------------------

from ipc import matriz

M = matriz.cria_matriz(12, 12)
soma = matriz.media_abaixo_diagonal_principal(M)
print(soma)
