#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Alexandre Marques Uchôa                   1715310028
# Carlos Eduardo Tapudima de Oliveira	    1715310030
# Gabriel de Queiroz Sousa                  1715310044
# Lucas Gabriel Silveira Duarte             1715310053
# Natália Cavalcantre Xavier                1715310021
#
# Lista1. Questão 12)Entrar  com  valores  inteiros  para  um  matriz  A4x4e  para  uma  matriz  B 4x4
# Gerar  e imprimir a SOMA (A+B).

a = []
b = []
soma = []
line = []

for i in range (4):
    for j in range(4):
        line.append(int(input("Digite o valor da matriz A na posiçao [%i,%i]:" %(i+1),(j+1))))
    a.append(line)
    line = []
print()

for i in range (4):
    for j in range(4):
        line.append(int(input("Digite o valor da matriz B na posiçao [%i,%i]:" %(i+1),(j+1))))
    b.append(line)
    line = []
print()

for linha in range(4):
    for coluna in range (4):
        line.append(a[linha][coluna] + b[linha][coluna])
    soma.append(line)
    line = []
print()

for line in soma:
    print(line)

