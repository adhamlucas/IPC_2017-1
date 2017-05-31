#---------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Jandinne Duarte de Oliveira                   1015070265
# Wesley da Silva Rocha                         1715310026 
#
# Faça um procedimento que receba o vetor de registro definido no
# exercício anterior, por parâmetro, e retorna também por
# parâmetro: a maior idade entre os habitantes e a quantidade de
# individuos do sexo feminino cuja idade está entre 18 e 35
# (inclusive) e que tenham olhos verdes e cabelos louros.
# 
#---------------------------------------------------------------------

from ipc import vetor
dados = vetor.le_dados()
print(vetor.crivo_de_dados(dados))
