# ---------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Antônio Diego Furtado da Silva        1715310004
# Aracille de Souza Barbosa             1315120206
# Marcus Vinicius Paes da Silva Santos  1515070060
# Silas Castro de Mendonça              1715310066
# Wesley da Silva Rocha                 1715310026
#
# Um armazém trabalha com 100 mercadorias diferentes identificadas
# pelos números inteiros de 1 a 100. O dono do armazém anota a
# quantidade de cada mercadoria vendida durante o mês. Ele tem uma
# tabela que indica, para cada mercadoria, o preço de venda. Escreva
# um algoritmo em PORTUGOL para calcular o faturamento mensal do
# armazém. A tabela de preços é fornecida seguida pelos números das
# mercadorias e as quantidades vendidas. Quando uma mercadoria não
# tiver nenhuma venda, é informado o valor zero no lugar da quantidade.
#
# ---------------------------------------------------------------------

tabela = 101*[None]
for i in range(100):
    entrada = input().split()
    valor = float(entrada[0])
    mercadoria = int(entrada[1])
    try:
        quantidade = int(entrada[2])
    except IndexError:
        quantidade = 0
    tabela[mercadoria] = [valor, quantidade]

total = 0
for mercadoria in tabela:
    try:
        total += mercadoria[0]*mercadoria[1]
    except TypeError:
        pass
print(total)
