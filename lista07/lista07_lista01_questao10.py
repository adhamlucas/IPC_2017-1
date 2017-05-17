# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Enrique Leão Barbosa Izel         1715310048
# Hugo Thadeu Silva Cardoso         1715310013
# Victor Summer Oliveira Pantaleao  1715310042
# Wilbert Luís Evangelista Marins   1715310055
# Yuri Leandro de Aquino Silva      1615100462
#
# Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
# somente os elementos abaixo da diagonal secundária.
#---------------------------------------------------------------------------------

a =[]
b =[]
c =[]
d =[]
e =[]
f =[]
g =[]
h =[]
i =[]
j =[]

cont = 1
cont2 =1
cont3 =1
cont4 =1
cont5 =1
cont6 =1
cont7 =1
cont8 =1
cont9 =1
cont10 =1

while cont <= 10:
    number1 = int(input("Digite o elemento1: "))
    a.append(number1)
    cont += 1

while cont2 <= 10:
    number2 = int(input("Digite o elemento2: "))
    b.append(number2)
    cont2 += 1

while cont3 <= 10:
    number3 = int(input("Digite o elemento3: "))
    c.append(number3)
    cont3 += 1

while cont4 <= 10:
    number4 = int(input("Digite o elemento4: "))
    d.append(number4)
    cont4 += 1

while cont5 <= 10:
    number5 = int(input("Digite o elemento5: "))
    e.append(number5)
    cont5 += 1

while cont6 <= 10:
    number6 = int(input("Digite o elemento6: "))
    f.append(number6)
    cont6 += 1

while cont7 <= 10:
    number7 = int(input("Digite o elemento7: "))
    g.append(number7)
    cont7 += 1

while cont8 <= 10:
    number8 = int(input("Digite o elemento8: "))
    h.append(number8)
    cont8 += 1

while cont9 <= 10:
    number9 = int(input("Digite o elemento9: "))
    i.append(number9)
    cont9 += 1

while cont10 <= 10:
    number10 = int(input("Digite o elemento10: "))
    j.append(number10)
    cont10 += 1


print (b[9])
print (c[8:10])
print (d[7:10])
print (e[6:10])
print (f[5:10])
print (g[4:10])
print (h[3:10])
print (i[2:10])
print (j[1:10])