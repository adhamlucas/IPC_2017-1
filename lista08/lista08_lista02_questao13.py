#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Gabriel de Queiroz Sousa                  1715310044
# Lucas Gabriel Silveira Duarte             1715310053
# Ian Gabriel Costa Machado                 1215120276
# Rodrigo Duarte de Souza                   1115140049
# 
#Faça um procedimento que recebe, por parâmetro,
# um vetor A(25) de inteiros e substitui todos os valores negativos de A por zero.
#  O vetor A deve retornar alterado.
#----------------------------------------------------------------------------------------------------------------------
from ipc import vetor

def substituir_negativos_por_zero(vetor):
    for i,x in enumerate(vetor):
        if x < 0:
            vetor[i] = 0

    return vetor

vetor = vetor.criar_vetor_tamanho25()

vetor = substituir_negativos_por_zero(vetor)

print(vetor)
