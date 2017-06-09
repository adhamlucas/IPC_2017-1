# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros                      1715310043
# Gabriel Nascimento de Oliveira            1715310052
# Luiz Daniel Raposo Nunes de Mello	        1715310049
# Tiago Ferreira Aranha 	                1715310047
# Wilbert Luís Evangelista Marins           1715310055
# Mackson Garcez Moreno de Oliveira júnior  1215090300
#
# 21.Faça um programa que receba o número e horas trabalhadas
# Faça um programa que receba o número de horas trabalhadas,
# o valor do salário mínimo e o número de horas extras trabalhadas,
# calcule e mostre o salário a receber, seguindo as regras abaixo:
#
# a) A hora trabalhada vale 1/8 do salário mínimo;
# b) A hora extra vale 1/4 do salário mínimo
# c) O salário bruto equivale ao número de horas trabalhadas
#    multiplicado pelo valor da hora trabalhada;
# d) A quantia a receber pelas horas extras equivale ao número
#    de horas extras trabalhadas multiplicado pelo valor das horas extras;
# e) O salário a receber equivale ao salário bruto mais a quantia
#    a receber pelas horas extras
# ----------------------------------------------------------

hour_worked = int(input('Quantas horas você trabalhou?'))
minimal_salary = float(input('Qual o valor do salário mínimo?'))
extra_hours_worked = int(input('Quantas horas extras você trabalhou?'))

value_hour_worked = minimal_salary * 1 / 8
value_extra_hours_worked = minimal_salary * 1 / 4
grossy_salary = hour_worked * value_hour_worked
grossy_extra = extra_hours_worked * value_extra_hours_worked
salary = grossy_extra + grossy_salary

print('Salário %.2f' % salary)
