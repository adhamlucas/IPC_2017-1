#--------------------------------------------------------------------------
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
#Gabriel Barroso da Silva Lima     1715310011
#Felipe Eduardo Silva de Almeida   1715310031
#Frederico Victor Alfaia Rodrigues 1515200030
#Diogo Roberto Duarte da Costa     1715310056
#Felipe Guerreiro de Mello         1315120052
#Faça um Programa que peça dois números e imprima o maior deles. 
#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#
#                          Até 5 Kg           Acima de 5 Kg
#    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da 
# promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no 
# cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total a compra. Escreva um 
# programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, 
# valor do desconto e valor a pagar. 
#-------------------------------------------------------------------------------------

carne = int(input("1 - File Duplo | 2 - Alcatra | 3 - Picanha"))
quant = int(input("Quantidade desejada(em quilos)"))
tab = int(input("Tem o cartão Tabajara? (1 - sim | 0 - não)"))
print("")
print("--- CUPOM FISCAL ----")
print("")
if quant <= 5:
	if carne == 1:
		preco = quant*4.9
		print("Tipo da carne: File Duplo")
	else:
		if carne == 2:
			preco = quant*5.9
			print("Tipo da carne: Alcatra")
		else: 
			preco=quant*6.9
			print("Tipo da carne: Picanha")
else:
	if carne == 1:
		preco = quant*5.8
		print("Tipo da carne: File Duplo")
	else:
		if carne == 2:
			preco = quant*6.8
			print("Tipo da carne: Alcatra")
		else:
			preco = quant*7.8
			print("Tipo da carne: Picanha")
if tab == 1:
	desco = preco*0.05
	print("Tipo do pagamento: cartão")
else:
	desco = 0
	print("Tipo do pagamento: dinheiro")
print("Quantidade:", quant, "Kg")
print("Preco total:", preco)
print("Valor do desconto:", desco)
print("Valor a pagar:", preco-desco)
