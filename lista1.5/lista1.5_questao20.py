# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros                      1715310043
# Gabriel Nascimento de Oliveira            1715310052
# Luiz Daniel Raposo Nunes de Mello	        1715310049
# Tiago Ferreira Aranha 	                  1715310047
# Wilbert Luís Evangelista Marins           1715310055
# Mackson Garcez Moreno de Oliveira júnior  1215090300
#
# 20. Faça um programa que receba a medida do ângulo formado por uma escada apoiada no chão
# e a distância que a escada está da parede. Calcule e mostre a medida da escada para que se
# possa alcançar a ponta da escada.
# ----------------------------------------------------------

angle = int(input('informe o angulo'))
distance = int(input('informe a distancia'))

import math

measure = distance / math.cos(math.radians(angle))

print('distancia %.2f' % measure)