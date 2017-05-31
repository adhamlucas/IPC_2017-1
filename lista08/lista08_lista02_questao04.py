#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Fang Yao                           1115180236
# Enrique leão Barbosa               1715310048
# Hugo Thadeu Silva Cardoso          1715310013
# Victor Summer Oliveira             1715310042
# Wilbert Luis Evangelista Marins    1715310055
# Guilherme Silva de Oliveira        1715310034
# Luis Gustavo Moura de Queiroz      1715310037

# 04. Faça um procedimento que recebe por parâmetro os valores necessário para o cálculo da fórmula de báskara e retorna, 
# também por parâmetro, as suas raízes, caso seja possível calcular. 
#----------------------------------------------------------------------------------------------------------------------


from math import sqrt

def baskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    return (- b + sqrt(delta))/ (2 * a) , (- b - sqrt(delta))/ (2 * a)

a = int(input())
b = int(input())
c = int(input())

rã = baskara(a, b ,c)
print(rã)
