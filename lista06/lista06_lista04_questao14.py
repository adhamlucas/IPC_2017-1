#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Gabriel de Queiroz Sousa                1715310044
# Lucas Gabriel Silveira Duarte           1715310053
# Matheus de Oliveira Marques             1515310514
# Rodrigo Duarte de Souza                 1115140049
#
# Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras,
# como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337.
# O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet,
# sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise
# sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto
# e transforme-o para a grafia leet speak.
#---------------------------------------------------------------------------

leet = (('a', '4'), ('l', '1'), ('e', '3'), ('s', '5'), ('g', '6'), ('r', '12'), ('t', '7'), ('q', '9'))

sring = input("Informe palavra = ")
nova = sring
print("Inicialmente: ", sring)
for antigo, novo in leet:
    nova = nova.replace(antigo, novo)
print("Finalmente = ", nova)