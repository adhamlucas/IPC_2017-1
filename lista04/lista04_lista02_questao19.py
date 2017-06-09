#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# Vitor Summer Oliveira Pantaleão 	1715310042
# Vítor Simões Azevedo 			1715310025
# Wesley da Silva Rocha			1715310026
# Wilbert Luís Evangelista Marins 	1715310055
# Yuri Leandro de Aquino Silva 		1615100462
#
# Ler um valor inteiro, que é a duração em segundos de um determinado evento
# em uma fábrica, e informá-lo expresso em horas: minutos: segundos.
#------------------------------------------------------------------------------

time = int(input("Digite o tempo em segundos: "))
hour = time//3600
minutes = int((((time/3600)-hour)*60)//1)
seconds = round((((((time/3600)-hour)*60)-(((time/3600)-hour)*60)//1))*60)
print(hour,":",minutes,":",seconds)
