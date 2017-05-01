#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Gabriel de Queiroz Sousa                1715310044
# Lucas Gabriel Silveira Duarte           1715310053
# Matheus de Oliveira Marques             1515310514
# Rodrigo Duarte de Souza                 1115140049
#
#Nome ao contrário em maiúsculas.
# Faça um programa que permita ao usuário digitar o seu nome
# e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
#---------------------------------------------------------------------------


name = input("Digite seu nome(você pode utilizar letras maiúsculas e minúsculas): ")
name = name.upper()
print(name[::-1])