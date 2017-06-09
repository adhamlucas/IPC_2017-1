#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# Erik Atlio Silva Rey                  1715310059
# Edson de Lima Barros                  1715310043
# Enrique Leão Barbosa Izel             1715310048
# Evandro Padilha Barroso Filho         1715310009
# Fang Yao                              1115180236
#
#52.Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês
#do ano por extenso, em inglês, com a primeira letra maiúscula.
#Entrada:
#A entrada contém um único valor inteiro.
#Saída:
#Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.
#-----------------------------------------------------------------------------------------------------------------------

month = int(input())

month_list = ["January",   "February", "March",    "April",
     "May",       "June",     "July",     "August",
     "September", "October",  "November", "December"]
print(month_list[month-1])













