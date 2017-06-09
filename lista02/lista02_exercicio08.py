# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Carlos Eduardo Tapudima de Oliveira       1715310030
# Frederico Victor Alfaia Rodrigues         1515200030
# Joelson Pereira Lima	                    1715310060
# Lucas Gabriel Silveira Duarte             1715310053
# Reinaldo da Silva Vargas	            1715310054
# Walter Nobre da Silva Conceição           1715310057
#
# 8 - Explicar DETALHADAMENTE o funcionamento do programa abaixo:
#
#   import turtle
#   colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange']
#   t=turtle.Pen()
#   turtle.bgcolor('black')
#   for x in range(360)
#       t.pencolor(colors[x%6])
#       t.width(x/100+1)
#       t.foward(x)
#       t.left(59)
# ----------------------------------------------------------

import turtle #importa a biblioteca turtle
colors=['red', 'purple', 'blue','green', 'yellow', 'orange'] # cria um vetor de 6 posições do tipo string e armazena os nomes das cores uportadas pelo turtle
t=turtle.Pen() # instancia a janela gráfica do turtle
turtle.bgcolor('black') # muda a cor de fundo da janela grafica do turtle para preto
for x in range(360): # inicia um laço com a variavel x crencendo de 0 a 359
    t.pencolor(colors[x%6])# muda a cor da seta do turtle pegando o resto da divisão de x por 6
    t.width(x/100+1) # aumenta proporcionalmente a grossura do risco da turtle (em pixels) proporcional ao x
    t.forward(x) # turtle risca x pixels
    t.left(59) # a seta aponta para 59 graus a esquerda do angulo atual
