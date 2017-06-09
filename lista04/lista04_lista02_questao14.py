# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Guilherme Silva de Oliveira       1715310034
# Gabriel Nascimento de Oliveira    1715310052
# Gabriel de Queiroz Souza          1715310044
# Hugo Thadeu Silva Cardoso         1715310013
# Ian Gabriel Costa Machado         1215120276
#
#  Calcule o consumo médio de um automóvel sendo fornecidos
#  a distância total percorrida (em Km) e o total de combustível gasto (em litros).
# ----------------------------------------------------------------------------------------------------------------------
x = int(input())
y = float(input())
consumo = x / y
print('%.3f km/l' %consumo)