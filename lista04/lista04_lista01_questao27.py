#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# Vitor Summer Oliveira Pantaleão 	1715310042
# Vítor Simões Azevedo 			    1715310025
# Wesley da Silva Rocha			    1715310026
# Wilbert Luís Evangelista Marins 	1715310055
# Yuri Leandro de Aquino Silva 		1615100462
#
# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#
# Peso          |Até 5kg   |        |Acima de 5kg|
# Morango       |R$ 2,50/kg|        |R$ 2,20/kg  |
# Maçã          |R$ 1,80/kg|        |R$ 1,50/kg  |
#
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da
# compra ultrapassar R$ 25,00, receberá ainda um desconto de 10%
# sobre este total. Escreva um algoritmo para ler a quantidade
# (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
# e escreva o valor a ser pago pelo cliente.
#------------------------------------------------------------------------------

strawberry_kg = float(input('Insira quantidade de morangos (em kg):'))
apple_kg = float(input('Insira quantidade de maças (em kg):'))

total_price = 0
if strawberry_kg <= 5:
  total_price += 2.5*strawberry_kg
else:
  total_price += 2.20*strawberry_kg
if apple_kg <= 5:
  total_price += 1.8*apple_kg
else:
  total_price += 1.5*apple_kg
  
if strawberry_kg + apple_kg > 8 or total_price > 25:
  total_price -= 0.1*total_price
  
print('Total de valor à pagar:', total_price)
