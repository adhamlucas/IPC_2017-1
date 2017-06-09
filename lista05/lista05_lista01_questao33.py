#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058

# 33- O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
#  indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
#  bem como a média das temperaturas.

n = int(input("Quantas temperaturas serão informadas?\n"))
i = 0
temp =  int(input("Temperatura: "))
maior = temp
menor = temp
soma = temp
while i<n-1:
    temp =  int(input("Temperatura: "))
    if temp < menor:
        menor = temp
    if temp > maior:
        maior = temp
    soma+=temp
    i+=1
media = soma/n
print ("Maior temperatura: %d" % maior)
print ("Menor temperatura: %d" % menor)
print ("Média das temperaturas: %d" % media)