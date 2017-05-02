#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Alexandre Marques Uchôa           1715310028
# Carlos Eduardo T. de Oliveira     1715310030
# Hugo Thadeu Silva Cardoso         1715310013
# Judá Salazar Braga                1515200050
# Kethelen Tamara Braba Barbosa     1525212002
# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor
# que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos
# seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
l=[]
inicio=int(input("De qual valor: "))
lim=int(input("Até qual valor: "))
com=0
for com in range(100000000000):
    sal=200+(9*com)/100
    m= ["vendedor %d" %com , sal]
    l.append(m)
    if sal > lim:
        break
    if sal >= inicio:
        print(l[com])
print("Número de Vendedores (ou como quiser chamar) %d" %com)
print("Maior Salário do Povo: %d" %sal)
