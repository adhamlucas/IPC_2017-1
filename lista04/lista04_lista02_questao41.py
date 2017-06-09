#----------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Adham Lucas da Silva Oliveira         1715310059
# Alexandre Marques Uchôa               1715310028
# André Luís Laborda Neves              1515070006
# Carlos Eduardo Tapudima de Oliveira	1715310030
# Diego Reis Figueira                   1515070169
#
# Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas
# de um ponto em um plano. A seguir,
# determine qual o quadrante ao qual pertence o ponto, ou se está
# sobre um dos eixos cartesianos ou na origem (x = y = 0).
# Se o ponto estiver na origem, escreva a mensagem “Origem”.
# Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.
#----------------------------------------------------------------------------------

x , y = input().split()
x = float(x)
y = float(y)

if x == y == 0:
    print('Origem')
elif x > 0 < y:
    print('Q1')
elif x < 0 < y:
    print('Q2')
elif x < 0 > y:
    print('Q3')
elif x > 0 > y:
    print('Q4')
elif x == 0 != y:
    print('Eixo Y')
else:
    print('Eixo X')
