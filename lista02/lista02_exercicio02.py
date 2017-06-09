#-----------------------------------------------------------------------------------------------------------------------
#introdução a Programação de Computadores
#Prof. Jucimar Jr.
#Adham Lucas da Silva Oliveira       1715310001
#Erik Atilio Silva Rey               1715310059
#Enrique Leão Barbosa Izel           1715310048
#Guilherme Silva de Oliveira         1715310034
#Lukas Michel Souza Mota             1715310018
#Ulisses Antonio  Antonino da Costa  1515090555
#
#Desenhar um polígono com 3 lados iguais. Cada lado uma cor diferente.
#-----------------------------------------------------------------------------------------------------------------------
import turtle                           #importando a tartaruga
colors=['purple', 'blue', 'orange']     #definindo as cores
t=turtle.Pen()                          #simbolizando que a caneta da tartaruga significa t
turtle.bgcolor('black')                 #definindo a cor de fundo
for x in range(3):                      #quantidade de linhas que a tartaruga desenhará
    t.pencolor(colors[x%3])             #quais cores ela utilizará
    t.forward(100)                      #a distancia que a tartaruga avançará
    t.left(120)                         #o angulo que a a tartaruga irá se mover à esquerda
