# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Alexandre Marques Uchôa           1715310028
# Carlos Eduardo T. de Oliveira     1715310030
# Hugo Tadeu Silva Cardoso          1715310013
# Judá Salazar Braga                1515200050
# Kethelen Tamara Braba Barbosa     1525212002
#
# Faça um programa para resolver o seguinte problema:
# São dadas as coordenadas reais x e y de um ponto,
#  um número natural n, e as coordenadas reais de n pontos (1 < n < 100).
#  Deseja-se calcular e imprimir sem repetição os raios das
#  circunferências centradas no ponto (x,y) que passam por pelo menos um
#  dos n pontos dados.
#
# Exemplo: (x,y) = (1.0, 1.0) ; n = 5
# pontos : (-1.0, 1.2) , (1.5, 2.0) , (0.0, -2.0) , (0.0, 0.5) , (4.0, 2.0)
# Nesse caso há três circunferências de raios: 1.12,  2.01 e 3.162.

import math

x_center = float(input('Digite o valor real de X centro: '))
y_center = float(input('Digite o valor real de Y centro: '))
n = int(input('Digite a quantidade de coordenadas que deseja submeter: '))

x = [0] * n
y = [0] * n
rays = [0] * n
count = 0

while count < n:
    x[count] = float(input('Entre com o X %i :' % (count + 1)))
    y[count] = float(input('Entre com o Y %i :' % (count + 1)))
    a = (x_center - x[count])**2
    b = (y_center - y[count])**2
    rays[count] = round(math.sqrt(a + b), 3)
    count += 1

count = 0
rays_2 = []

while count < n:
    ray = rays[count]
    appeared = 1
    count_2 = count + 1

    while count_2 < n:

        if (ray == rays[count_2]):
            appeared += 1

        count_2 +=1

    if (appeared != 1):
        rays_2.append(ray)

    count += 1

print(rays_2)