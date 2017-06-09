# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Tiago Ferreira Aranha                     1715310047
# Victor Hugo de Oliveira Carreira          1715310063
# Ulisses Antonio Antonino da Costa         1515090555  
#
# URI Online Judge | 1048
# Aumento de Salário
#
# A empresa ABC resolveu conceder um aumento de salários a seus 
# funcionários de acordo com a tabela abaixo:
#
#   Salário				    Percentual de Reajuste
#   0-400.00			    15%
#   400.01-800.00		    12%
#   800.01-1200.00		    10%
#   1200.01-2000.00		    7%
#   Acima de 2000		    4%
#
#
# Leia o salário do funcionário e calcule e mostre o novo salário, 
# bem como o valor de reajuste ganho e o índice reajustado, em percentual.
#
# Entrada
# 
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
#
# Saída
# 
# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o 
# percentual de reajuste ganho, conforme exemplo abaixo.
#
# --------------------------------------------------------------------------------------

salary = float(input())

if (0 < salary <= 400.00):
    increase_percentual = 0.15
elif (400.01 < salary <= 800.00):
    increase_percentual = 0.12
elif (800.01 < salary <= 1200.00):
    increase_percentual = 0.10
elif (1200.01 < salary <= 2000.00):
    increase_percentual = 0.07
else:
    increase_percentual = 0.04

print("Novo salario: %5.2f" % (salary + salary * increase_percentual))
print("Reajuste ganho: %5.2f" % (salary * increase_percentual))
print("Em percentual: %d" % (increase_percentual * 100), "%")
