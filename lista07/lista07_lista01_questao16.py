#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Adham Lucas da Silva Oliveira                 1715310001
# Jandinne Duarte de Oliveira                   1015070265
# Roberta de Oliveira da Cruz                   0825070169
# Nayara da Silva Cerdeira da Costa             1715310038
# Wesley da Silva Rocha                         1715310026 
#
#3Uma floricultura conhecedora de sua clientela gostaria de fazer um algoritmo que
#pudesse controlar sempre um estoque mínimo de determinadas plantas, pois todo dias,
#pela manhã, o dono faz novas aquisições. Criar um algoritmo que deixe cadastrar 50
#tipos de plantas e nunca deixar o estoque ficar abaixo do ideal. Para cada planta, o
#dono gostaria de cadastrar o nome, o estoque ideal e a quantidade em estoque. Dessa
#forma o algoritmo pode calcular a quantidade que o dono da loja precisa comprar no
#próximo dia. Essa quantidade a ser comprada deve ser impressa (quando maior que
#zero) como uma lista para o dono da floricultura.
#---------------------------------------------------------------------------------------
matriz = []
estoque_necessario = []
limite = 3

for x in range(3):
    things = input('Digite as informações (Nome/Est. Ideal/Qtd. Estoque: ').split()
    matriz.append(things)

for i, element in enumerate(matriz):
    linha = []
    if int(element[2]) < int(element[1]):
        necessary = int(element[1]) - int(element[2])
        linha.append(element[0])
        linha.append(necessary)
        estoque_necessario.append(linha)

print(estoque_necessario)
