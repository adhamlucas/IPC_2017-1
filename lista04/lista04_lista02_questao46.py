#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# Vitor Summer Oliveira Pantaleão   1715310042
# Vítor Simões Azevedo              1715310025
# Wesley da Silva Rocha             1715310026
# Wilbert Luís Evangelista Marins   1715310055
# Yuri Leandro de Aquino Silva      1615100462
#
# Leia a hora inicial e a hora final de um jogo. A seguir calcule a
# duração do jogo, sabendo que o mesmo pode começar em um dia e terminar
# em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
#------------------------------------------------------------------------------

begin, end = map(int, input().split())
total_time = 24 - begin + end
total_time %= 24
if (total_time == 0): time = 24
  
print('O JOGO DUROU %d HORA(S)' %total_time)
