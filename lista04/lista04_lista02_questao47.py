
#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Reinaldo da Silva Vargas 1715310054
# Natalia Cavalcante Xavier 1715310021
# Nayara da Silva Cerdeira da Costa 1715310038
# Marcus Vinicius Paes da Silva Santos 1515070060
# Matheus de Oliveira Marques 1515310514
#
# Faça um programa que peça as horas iniciais,minutos iniciais,horas finais e minutos finis de um jogo. em seguida imprima na tela
# a soma da partida do jogo
#--------------------------------------------------------------------------

start_hour = float(input('informe a hora inicial'))
start_minute = int(input('informe o minuto inicial'))
end_hour = int(input('informe a hora final'))
end_minute = int(input('informe o minuto final'))

total_hour = (start_hour + end_hour)
total_minute = (start_minute + end_minute)

print('O jogo durou:', total_hour, 'horas', 'e', total_minute, 'minutos')
