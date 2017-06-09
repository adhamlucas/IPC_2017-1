# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Aracille de Souza Barbosa           1315120206
# Felipe Eduardo Silva de Almeida     1715310031
# Kethelen Tamara Braga               1525212002
# Nayara da Silva Cerdeira da Costa   1715310038
# Vitor Summer Oliveira Pantaleão     1715310042
# Yuri Leandro de Aquino Silva        1615100462
#
# Faça um programa que receba o valor do salário mínimo e o
# valor do salário de um funcionário, calcule e mostre a quantidade
# de salários mínimos que ganha esse funcionário.
#-----------------------------------------------------------

s_minimum = float(input("Informe o salário mínimo: "))                    # Usuário insere o valor do salário mínimo
s_employee = float(input("Informe salário do funcionário: "))             # Usuário insere o valor do salário do funcionário
amount_sm = s_employee/s_minimum                                          # Fórmula para calcular a quantidade de salários mínimos recebidos
print ("A quantidade de salarios minimos recebidos é: %.2f" % amount_sm)  # Imprime a quantidade de salários mínimos que o funcinário recebe
