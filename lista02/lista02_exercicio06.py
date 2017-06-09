# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Hugo Thadeu Silva Cardoso	         1715310013
# Luiz Paulo Machado	             1515200542
# Ian Gabriel Costa Machado          1215120276
# André Luis Laborda Neves	         1515070006
# Gabriel de Queiroz Souza           1715310044
# João Vitor De Cordeiro B Gonçalves 1515140036
#6) Desenhar uma estrela de 6 pontas
# ----------------------------------------------------------
import turtle as tu

def draw_star(x, y, side):
    star_angle = 360.0/6
    left_angle = star_angle * 2
    tu.penup()
    tu.goto(x, y)
    tu.pendown()
    for i in range(6):
        tu.forward(side)
        tu.right(star_angle)
        tu.forward(side)
        tu.left(left_angle)

tu.speed('fast')
tu.color('blue')
tu.width(2)
x = -150
y = -50
side = 100
draw_star(x, y, side)
tu.mainloop()
