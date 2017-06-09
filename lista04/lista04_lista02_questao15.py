#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# João Vitor de Cordeiro B. Gonçalves   1515140036
# Joelson Pereira Lima                  1715310060
# Judá Salazar Braga                    1515200050
# Kethelen Tamara Braga Barbosa         1525212002
# Lucas Gabriel Silveira                1715310053
# Silas Castro de Mendonça              1715310066
# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:
#------------------------------------------------------------------------------

line1 = (input().split())
line2 = (input().split())
x1 = line1
y1 = line1
x2 = line2
y2 = line2
distance = ((((float(x2)-float(x1))**2)+((float(y2)-float(y1))**2))**0.5)

print('%0.4f'%distance)
