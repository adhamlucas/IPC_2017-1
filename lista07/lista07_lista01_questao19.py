#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Alexandre Marques Uchôa                   1715310028
# Carlos Eduardo Tapudima de Oliveira	    1715310030
# Gabriel de Queiroz Sousa                  1715310044
# Lucas Gabriel Silveira Duarte             1715310053
# Natália Cavalcantre Xavier                1715310021
#
# Lista 01. Questão 19) Criar um algoritmo que possa armazenar
# as alturas de dez atletas de cinco delegações que participarão
# dos jogos de verão. Imprimir a maior altura de cada delegação.

athletes = []
line = []
aux = 0

for i in range(0,5):

    for j in range(0,10):

        line.append(float( input('Digite a altura do atleta número %i da delegação %i: ' % ((j + 1),(i + 1)) )))


    athletes.append(line)
    line = []
    print()

aux = 1
big_ath = 0.0

for delegation in athletes:

    big_ath = max(delegation)
    print('Maior altura da delegação %i = %.2f m' % (aux,big_ath))
    aux += 1