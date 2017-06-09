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
# Faça um programa que lê o nome de um vendedor, seu salário fixo e o
# total da venda feito por ele / ela mesma no mês (em dinheiro).
# Considerando que este vendedor recebe 15% sobre todos os produtos,
# escrever o salário final (total) deste vendedor no final 
# do mês, com duas casas decimais.
#------------------------------------------------------------------------------

name = input()
salary = float(input())
sales_amount = float(input())
final_salary = salary+((15/100)*sales_amount)
print("total = R$ {0:.2f}".format(final_salary))
