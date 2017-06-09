#----------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira             1715310001
# Frederico Victor Alfaia Rodrigues         1515200030
# Gabriel Barroso da Silva Lima             1715310011
# Nayara da Silva Cerdeira da Costa         1715310038
# Yuri Leandro de Aquino Silva              1615100462
#
# 20. Faça um procedimento que receba, por parâmetro,
#  um vetor K(15) e retorna, também por parâmetro,
# um vetor P contendo apenas os valores primos de K
#--------------------------------------------------

from ipc import vetor

vetor = vetor.criar_vetor_tamanho15()

P = vetor.criar_vetor_primo(vetor)

print(P)
