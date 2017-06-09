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
# Faça uma função que recebe, por parâmetro, uma matriz A(7, 6) e
# retorna a soma dos elementos da linha 5 e da coluna 3.
# 
#---------------------------------------------------------------------

from ipc import matriz

M = matriz.cria_matriz(7, 6)
soma = matriz.soma_matriz_parcial(M, 5, 3)
print(soma)
