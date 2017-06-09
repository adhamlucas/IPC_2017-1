#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# João Vitor de Cordeiro B. Gonçalves   1515140036
# Joelson Pereira Lima                  1715310060
# Judá Salazar Braga                    1515200050
# Kethelen Tamara Braga Barbosa         1525212002
# Lucas Gabriel Silveira                1715310053
# Silas Castro de Mendonça              1715310066
#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro
#valor deve aparecer valor inválido. .

dia = int(input("Digite um numero de 1 a 7: "))
if dia == 1 or dia == 2 or dia == 3 or dia == 4 or dia == 5 or dia == 6 or dia == 7:
	if dia == 1:
		print("DOMINGO")
	if dia == 2:
		print("SEGUNDA")
	if dia == 3:
		print("TERÇA")
	if dia == 4:
		print("QUARTA")
	if dia == 5:
		print("QUINTA")
	if dia == 6:
		print("SEXTA")
	if dia == 7:
		print("SABADO")
else:
	print("O numero digitado é invalido")
