#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Alexandre Marques Uchôa                   1715310028
# Carlos Eduardo Tapudima de Oliveira	    1715310030
# Gabriel de Queiroz Sousa                  1715310044
# Lucas Gabriel Silveira Duarte             1715310053
# Natália Cavalcante Xavier                1715310021
#
# Lista 01. Questao 20) Criar um algoritmo que carregue uma matriz 12 x 4 com os valores das vendas de uma
# loja, em que cada linha represente um mês do ano, e cada coluna, uma semana do mês.
# Para fins de simplificação considere que cada mês possui somente 4 semanas. Calcule
# e imprima:
# - Total vendido em cada mês do ano;
# - Total vendido em cada semana durante todo o ano;
# - Total vendido no ano.

meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho',
         'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
year = []
week = []

for month in range(0,12):

    for we in range(0,4):

        week.append(float(input('Mês %s | Semana %i R$ ' % (meses[month],(we + 1)))))

    year.append(week)
    week = []

wee = 1
acm_week = 0
acm_year = 0
mes = 0

# Recebendo o total arrecadado no mês
for month in year:

    for x in month:
        print('Arrecadação da semana %i R$ %.2f ' % (wee,x), end= '| ')
        acm_week += x
        wee += 1
    print()
    print('Total arrecadado no mês de %s R$ %.2f ' % (meses[mes],acm_week))
    print()
    acm_year += acm_week
    acm_week = 0
    mes += 1

print('Total recebido no ano R$ %.2f ' % acm_year)
