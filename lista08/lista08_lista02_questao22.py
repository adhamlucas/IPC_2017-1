# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros   1715310043
# Tiago Ferreira Aranha  1715310047
# Vitor Simôes Azevedo   1715310025
# Roberta de Oliveira da Cruz   0825070169
# Uriel Brito Barros            1515120558
#
# 22. Faça um procedimento que receba, por parâmetro um vetor B(50) de reais e
# calcula o maior valor do vetor.
#
# A seguir, o procedimento deve dividir
# todos os elementos de B pelo maior encontrado.
# O vetor deve retornar alterado.


from lista08.ipc import vetor

vetor1 = vetor.cria_vetor_numeros_decimais(50)

maior = vetor.maior_valor_do_vetor(vetor1)

vetor_final = vetor.divide_todos_por_numero(vetor1, maior)

print(vetor_final)
