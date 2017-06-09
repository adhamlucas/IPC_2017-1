#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# FANG YAO                                1115180236
# LUIZ PAULO MACHADO E SOUZA              1515200542
# FELIPE GUERREIRO DE MELLO               1315120052
# YURI LEANDRO DE AQUINO SILVA            1615100462  
#
#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
#---------------------------------------------------------------------------

n1=float(input('Digite um numero:'))
n2=float(input('digite o segundo numero:'))
n3=float(input('digite o terceiro numero:'))
n4=float(input('digite o ultimo numero:'))

media=float((n1+n2+n3+n4))/ int(4)
print('o primeiro numero:',n1)
print('o segundo numero:',n2)
print('o terceiro numero:',n3)
print('o ultimo numero:',n4)
print('a media dos 4 numeros:',media)
