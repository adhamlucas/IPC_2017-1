# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Antonio Diego Furtado da Silva        1715310004
# Fang Yao                              1115180236
# Juda Salazar Braga                    1515200050
# Matheus de Oliveira Marques           1515310514
# Vitor Simoes Azevedo                  1715310025
# Natalia Cavalcante Xavier             1715310021
# Desenhar uma estrela de 5 pontas
# ----------------------------------------------------------

import turtle

c = turtle.Pen()
d = turtle.Screen()

# muda o cursor para uma tartaruga
c.shape('turtle')

size = 250

# muda posicao inicial
c.penup()
c.goto(-130,50)
c.pendown()

for i in range(5):
    c.forward(size)
    c.right(144)

# aguarda a tela ser fechada pelo usuário
d.exitonclick()
