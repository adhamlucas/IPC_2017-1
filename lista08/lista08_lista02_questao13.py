#Faça um procedimento que recebe, por parâmetro,
# um vetor A(25) de inteiros e substitui todos os valores negativos de A por zero.
#  O vetor A deve retornar alterado.
from ipc import vetor

def substituir_negativos_por_zero(vetor):
    for i,x in enumerate(vetor):
        if x < 0:
            vetor[i] = 0

    return vetor

vetor = vetor.criar_vetor_tamanho25()

vetor = substituir_negativos_por_zero(vetor)

print(vetor)
