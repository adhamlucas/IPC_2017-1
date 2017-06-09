#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Joelson Pereira Lima 			    1715310060
# Gabriel Nascimento de Oliveira 	1715310052
# Hugo Thadeu Silva Cardoso         1715310013
# Jandinne Duarte de Oliveira 		1015070265
# Gabriel de Queiroz Souza		    1715310044
# Guilherme Silva de Oliveira		1715310034
#
# 28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada
# um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um. 
#---------------------------------------------------------------------------

quantidade_de_cds = int(input("Informe a quantidade de CDs: "))

c = 1
valor_total_gasto = 0

while c <= quantidade_de_cds:

    valor_cd = float(input("Valor do {}º CD: ".format(c)))
    valor_total_gasto = valor_total_gasto + valor_cd

    c += 1

valor_medio_gasto = valor_total_gasto / quantidade_de_cds

print("Valor total investido: %5.2f" % valor_total_gasto)
print("Valor médio gasto em cada CD: %5.2f" % valor_medio_gasto)
