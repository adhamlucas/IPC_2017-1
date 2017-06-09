#-----------------------------------------------------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Alexandre Marques Uchôa               1715310028
#Jandinne Duarte de Oliveira           1015070265
#Uriel Brito Barros                    1515120558
#Roberta de Oliveira da cruz           0825070169
#Evandro Padilha Barroso Filho         1715310009
#
##
#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#a)Para homens: (72.7*h) - 58
#b)Para mulheres: (62.1*h) - 44.7 (h = altura)
#c)Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
#-----------------------------------------------------------------------------------------------------------------------
h = float(input('Digite sua altura em metros'))
p = float(input('Digite seu peso em quilos'))
sex = input('Você e homem ou mulher?')
if sex == 'homem':
    weight =  (72.7*h) - 58
    if weight > p:
        print ('Você esta abaixo do peso')
    if weight < p:
        print ('Você está acima do peso')
    if weight == p:
        print ('Você está no peso ideal')
if sex == 'mulher':
    weight = (62.1*h) - 44.7
    if weight > p:
        print ('Você esta abaixo do peso')
    if weight < p:
        print ('Você está acima do peso')
    if weight == p:
        print ('Você está no peso ideal')