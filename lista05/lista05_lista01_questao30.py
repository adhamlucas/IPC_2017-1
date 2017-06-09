# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Lukas Michel Souza Mota               1715310018
# Marcus Viniciius Paes da Silva Santos 1515070060
# Matheus de Oliveira Marques           1515310514
# Natália Cavalcante Xavier             1715310021
# Nayara da Silva Cerdeira da Costa     1715310038
#
#30. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães,
# a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
#Preço do pão: R$ 0.18
#Panificadora Pão de Ontem - Tabela de preços
#1 - R$ 0.18
#2 - R$ 0.36
#...
#50 - R$ 9.00
#----------------------------------------------------------
x = 1

price = float(input("Preço do pão: "))

while x <= 50:
    print("%02d - R$ %.2f" %(x, price * x))
    x = x + 1
