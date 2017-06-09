#------------------------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Prof. Jucimar Jr.
#Adham Lucas da Silva Oliveira       1715310001
#Erik Atilio Silva Rey               1715310059
#Enrique Leão Barbosa Izel           1715310048
#Ulisses Antonio  Antonino da Costa  1515090555
#Lukas Michel Souza Mota             1715310018
#Guilherme Silva de Oliveira         1715310034
#
#Tendo como dados de entrada a altura de uma pessoa,
#construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula: (72.7*altura) - 58
#------------------------------------------------------------
print ('-Saiba seu peso ideal-')
height = float(input('Digite sua altura em metros'))
weigh_ideal = ((72.7*height)-58)
print ('Seu peso ideal é:',weigh_ideal)