# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Hugo Thadeu Silva Cardoso          1715310013
# Luiz Paulo Machado                 1515200542
# Ian Gabriel Costa Machado          1215120276
# André Luis Laborda Neves           1515070006
# Gabriel de Queiroz Souza           1715310044
# João Vitor De Cordeiro B Gonçalves 1515140036
# Rodrigo Duarte de Souza            1115140049

# --------------------------


#ENTRADA DOS DADOS#####
horas = int(input(' Digite a hora: '))
minutos = int(input(' Digite os minutos: '))

#PROCESSAMENTO######

# LETRA A #
hmin = horas * 60
print('Conversão de horas para minutos =', hmin)

#LETRA B#
tminutos = hmin + minutos
print('Total em minutos =', tminutos)

#LETRA C#
segundos = tminutos * 60
print('Horas em segundos =', segundos)


