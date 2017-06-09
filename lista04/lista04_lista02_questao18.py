# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Tiago Ferreira Aranha                     1715310047
# Victor Hugo de Oliveira Carreira          1715310063
# 
# URI Online Judge | 1018
# Banknotes

# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) 
# no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
# A seguir mostre o valor lido e a relação de notas necessárias.
#
# Entrada
#
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
#
# Saída
#
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, 
# conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, 
# caso contrário seu programa apresentará a mensagem: “Presentation Error”.
# --------------------------------------------------------------------------------------

value = int(input())

print(value)
print("%i nota(s) de R$ 100,00" % int(value / 100))
value = value % 100
print("%i nota(s) de R$ 50,00" % int(value / 50))
value = value % 50
print("%i nota(s) de R$ 20,00" % int(value / 20))
value = value % 20
print("%i nota(s) de R$ 10,00" % int(value / 10))
value = value % 10
print("%i nota(s) de R$ 5,00" % int(value / 5))
value = value % 5
print("%i nota(s) de R$ 2,00" % int(value / 2))
value = value % 2
print("%i nota(s) de R$ 1,00" % int(value / 1))
value = value % 1
