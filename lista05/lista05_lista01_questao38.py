# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Prof. Jucimar Jr
#
# Lukas Michel Souza Mota               1715310018
# Marcus Viniciius Paes da Silva Santos 1515070060
# Matheus de Oliveira Marques           1515310514
# Natália Cavalcante Xavier             1715310021
# Nayara da Silva Cerdeira da Costa     1715310038
#
#38. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#Faça um programa que determine o salário atual desse funcionário.
#Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
#----------------------------------------------------------

salary = float(input("Informe o salário: "))
percentage = float(input("Informe a porcentagem: "))
year = int(input("Informe o ano: "))

while(year <= 2000):
    print("Ano:(",year,") Percentual:(",percentage,") Salario: R$",salary,"")
    salary += (salary * (percentage / 100.0))
    percentage *= 2
    year += 1

print("Salario atual do funcionario: R$",salary,"")
