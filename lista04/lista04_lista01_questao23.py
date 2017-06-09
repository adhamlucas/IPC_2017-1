#---------------------------------------------------------------------------------------------------------------------------
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
#
# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
#----------------------------------------------------------------------------------------------------------------------------

num = float(input("Digite o numero à ser analisado: "))
if round(num) == num:
	print("O número digitado é inteiro")
else:
	print("O número digitado é decimal")
