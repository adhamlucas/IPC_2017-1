#---------------------------------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Prof. Jucimar Jr.
#Adham Lucas da Silva Oliveira       1715310001
#Erik Atilio Silva Rey               1715310059
#Enrique Leão Barbosa Izel           1715310048
#Ulisses Antonio  Antonino da Costa  1515090555
#Lukas Michel Souza Mota             1715310018
#Guilherme Silva de Oliveira         1715310034
#
#Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#
#   salário bruto.
#    quanto pagou ao INSS.
#    quanto pagou ao sindicato.
#    o salário líquido.
#    calcule os descontos e o salário líquido, conforme a tabela abaixo:
#
#    + Salário Bruto : R$
#    - IR (11%) : R$
#    - INSS (8%) : R$
#    - Sindicato ( 5%) : R$
#    = Salário Liquido : R$
#----------------------------------------------------------------------
salary = float(input('Quanto você ganha por hora?'))
worked_hours = int(input('Quantas horas você trabalha por mês?'))
salary_gross = (salary*worked_hours)
tax_income = (salary_gross*0.11)
inss = (salary_gross*0.08)
syndicate = (salary_gross*0.05)
discount = (tax_income+inss+syndicate)
net_wage = (salary_gross-discount)

print('Seu salário Bruto é:R$',salary_gross)
print('Você pagou ao INSS:R$',inss)
print('VOcê pagou ao Sindicato:R$',syndicate)
print('Seu Salário Líquido é:R$',net_wage)