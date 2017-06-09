# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros                      1715310043
# Gabriel Nascimento de Oliveira            1715310052
# Luiz Daniel Raposo Nunes de Mello	        1715310049
# Renan de Almeida Campos                   0825060036
# Tiago Ferreira Aranha 	                1715310047
# Wilbert Luís Evangelista Marins           1715310055
# Mackson Garcez Moreno de Oliveira júnior  1215090300
#
# 4 - Desenhar um polígono com 6 lados iguais. Cada lado uma cor diferente
# ----------------------------------------------------------

import turtle

sides = 5

colors = ['orange', 'green', 'purple', 'blue', 'red', 'brown']


p = turtle.Pen()

for x in range(sides):
    p.pencolor(colors[x])
    p.forward(80)
    p.left(360 / sides)

turtle.mainloop()
