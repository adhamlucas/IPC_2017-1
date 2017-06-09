# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 08
# Victor Summer Oliveira Pantaleao 1715310042
# Walter Nobre Da Silva Conceição  1715310057
# Wesley da Silva Rocha            1715310026
# Wilbert Luís Evangelista Martins 1715310055
# Yuri Leandro de Aquino Silva     1615100462
#
# Dois ciclistas A e B estão andando em uma pista de ciclismo com 2 Km de
# comprimento com velocidades de 10 m/s e 15 m/s, respectivamente. Escreva um
# algoritmo em PORTUGOL que determine iterativamente o tempo que levará para que
# esses dois ciclistas A e B se encontrem em um mesmo ponto, sabendo que eles
# partiram de um mesmo ponto inicial, porém em sentido contrário. O algoritmo
# também deve calcular o deslocamento (a distância) que cada um percorreu.
# ----------------------------------------------------------

A = 0 # referene a partida do ponto incial
B = 2000 # refente a partida do ponto inicial (neste caso B partiu do contrário de A)
T = 0 # referente ao tempo inicial

while A < B:
    A = A + 10 # referente ao valor de A somado a + 10 (referente a sua velocidade em m/s)
    B = B - 15 # referente ao valor de b subtraido b - 15 (referente a sua velocidade em m/s (lembrando que partindo do contrário de A, logo será uma subtração))
    T = T + 1 # refente ao tempo t somado a mais 1 segundo a cada vez que o loop ocorre.

print("It was necessary ", T, " seconds to the meeting")
print("Cyclist A ran through: ", A, " meters")
print("While cyclist B ran: ", 2000 - B, " meters")
