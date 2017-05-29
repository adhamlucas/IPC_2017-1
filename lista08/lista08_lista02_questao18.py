# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros          1715310043
# Tiago Ferreira Aranha         1715310047
# Vitor Simôes Azevedo          1715310025
# Roberta de Oliveira da Cruz   0825070169
# Uriel Brito Barros            1515120558
#
# 17. Faça um procedimento que recebe, por parâmetro,
# 2 vetores de 10 elementos inteiros
# e que calcule e retorne, também por parâmetro,
# o vetor soma dos dois primeiros.


from lista08.ipc import vetor

vetor1 = vetor.cria_vetor(10)
vetor2 = vetor.cria_vetor(10)

vetor_diferenca = vetor.vetor_soma(vetor1, vetor2)

print(vetor_diferenca)
