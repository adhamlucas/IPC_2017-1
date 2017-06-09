# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Prof. Jucimar Jr
#
# Lukas Michel Souza Mota               1715310018
# Marcus Vinicius Paes da Silva Santos  1515070060
# Matheus de Oliveira Marques           1515310514
# Natália Cavalcante Xavier             1715310021
# Nayara da Silva Cerdeira da Costa     1715310038
#  
# Considere  uma  linha  ferroviária  entre  São  Paulo  e  Curitiba. 
# Suponha  que  uma locomotiva  (trem)  A  parte  de  São  Paulo  para 
# Curitiba  com  velocidade  de  30  m/s enquanto  que  uma  outra 
# locomotiva  B  parte  de  Curitiba  para  São  Paulo  no  mesmo 
# instante com velocidade de 40 m/s. Considere a distância entre São Paulo 
# e Curitiba de 400  Km.  Escreva  um  algoritmo  em  PORTUGOL  que  calcule 
# iterativamente  o  tempo necessário  para  os  maquinistas  pararem  as  locomotivas 
# antes  que  uma   colisão aconteça. 
# O  algoritmo  deve  calcular  também  a  distância  que  as  locomotivas  devem 
# percorrer para que a colisão aconteça
# ----------------------------------------------------------

a_speed = 30
b_speed = 40

distance = 400000
time = 0

while (distance) > 0:
    distance -= (a_speed + b_speed)
    time += 1

print("Os maquinistas devem parar dentro de: "),
print("%dh " % (time/3600)),
print("%dmin " % ((time % 3600) / 60)),
print("e %ds" % (time % 60))

a_distance = a_speed * time
b_distance = b_speed * time

print("Distancia percorrida pelas locomotivas:")
print("Locomotiva A: %d m" % a_distance)
print("Locomotiva B: %d m" % b_distance)
