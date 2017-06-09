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
#Faça um Programa que receba a quantidade de dinheiro em reais
#que uma pessoa que vai viajar possui. Essa pessoa vai passar
#por vários países e precisa converter seu dinheiro em dolares,
#marco alemao, libra esterlina. Sabe-se que a cotação do dola é R$ 1,80 ,
#o marco alemao é de R$ 2.00 e a Libra esterlina é de R$1,57.
#O programa deve fazer as conversõs e mostrá-las.
#----------------------------------------------------------------------
money = float(input('Com quanto dinheiro você vai viajar? R$:')
dollar = (money/1.8)
german_mark = (money/2)
pound_sterling = (money/1.57)

print('Você terá em dolares: U$', round(dollar, 2))
print('Você terá em Marco Alemão: DM', round(german_mark, 2))
print('Você terá em Libra Esterlina: £', round(pound_sterling, 2))
