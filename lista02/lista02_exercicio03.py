# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Aracille de Souza Barbosa           1315120206
# Felipe Eduardo Silva de Almeida     1715310031
# Kethelen Tamara Braga               1525212002
# Naiara da Silva Cedeira da Costa    1715310038
# Vitor Summer Oliveira Pantaleão     1715310042
# Yuri Leandro de Aquino Silva        1615100462
#
# Desenhar um polígono com 5 lados iguais.
# Cada lado uma cor diferente.
#  ----------------------------------------------------------

import turtle # importa a biblioteca turtle
colors=['red', 'purple', 'blue','green', 'yellow'] #cria um vetor de 5 posições do tipo string para cada lado do polígono
t=turtle.Pen() #
turtle.bgcolor('black') # muda a cor doefundo da janela para preto
for x in range(5): # inicia um laço de 0 até 4 para a criação de cada lado do poligno
