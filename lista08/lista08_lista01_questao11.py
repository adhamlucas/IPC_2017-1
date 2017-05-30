#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Fang Yao                           1115180236
# Enrique leão Barbosa               1715310048
# Hugo Thadeu Silva Cardoso          1715310013
# Victor Summer Oliveira             1715310042
# Wilbert Luis Evangelista Marins    1715310055
# Guilherme Silva de Oliveira        1715310034
#


# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D
# de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

dia, mes , ano =(input('data (DD/MM/AAA):')).split('/')
meses = {1:"Janeiro",2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho", 7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro",
         11:"Novembro", 12:"Dezembro"}
print('%s/%s/%s' %(dia,meses[int(mes) -1],ano))
