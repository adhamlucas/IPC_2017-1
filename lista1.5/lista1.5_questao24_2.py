#---------------------------------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Dayana Picanço Marquez         1715310058
#Felipe Guerreiro de Mello      1315120052
#Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que
#vai viajar possui. Essa pessoa vai passar por vários países e precisa converter seu dinheiro
#em dólares, marco alemão e libra esterlina. Sabe-se que a cotação do dólar é de R$1,80, do
#marco alemão é de R$2,00 e da libra esterlina é de R$1,57. O programas deve fazer as
#conversões e mostrá-las.
#----------------------------------------------------------------------

money = float(input())

dolar = money*1.8
german = money*2
brexit = money*1.57

print (dolar)
print (german)
print (brexit)
