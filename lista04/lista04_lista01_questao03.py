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
#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - 
#Masculino, Sexo Inválido.


print("Digite M para masculino e F para feminino")

gender = input("Digite \"M\" ou \"F\": ")

if gender == "M" or gender == "m":
	print("O gênero digitado foi MASCULINO")
else:
	if gender == "F" or gender == "f":
		print("O gênero digitado foi FEMININO")
	else:
		print("O gênero digitado é INVÁLIDO")
