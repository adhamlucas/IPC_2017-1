#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Adham Lucas da Silva Oliveira         1715310059
# Alexandre Marques Uchôa               1715310028
# André Luís Laborda Neves              1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Diego Reis Figueira                   1515070169
#
#Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
#-----------------------------------------------------------------------------------------------------------------------

days = int(input())

years = days//365
days = days - (years * 365)

months = days//30
days = days - (months * 30)

print(years,'ano(s)')
print(months,'mes(es)')
print(days,'dia(s)')
