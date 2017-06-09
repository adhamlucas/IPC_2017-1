# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros                      1715310043
# Gabriel Nascimento de Oliveira            1715310052
# Luiz Daniel Raposo Nunes de Mello	        1715310049
# Renan de Almeida Campos                   0825060036
# Tiago Ferreira Aranha 	                1715310047
# Wilbert Luís Evangelista Marins           1715310055
# Mackson Garcez Moreno de Oliveira júnior  1215090300
#
# 1.4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média
# ----------------------------------------------------------

result_1 = float(input('Informe a sua nota do primeiro bimestre:'))
result_2 = float(input('Informe a sua nota do segundo bimestre:'))
result_3 = float(input('Informe a sua nota do terceiro bimestre:'))
result_4 = float(input('Informe a sua nota do quarto bimestre:'))

average = (result_1 + result_2 + result_3 + result_4) / 4

print('Média dos quatro bimestres: %2.1f' % average)
