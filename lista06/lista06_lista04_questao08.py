#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Gabriel de Queiroz Sousa                1715310044
# Lucas Gabriel Silveira Duarte           1715310053
# Matheus de Oliveira Marques             1515310514
# Rodrigo Duarte de Souza                 1115140049
#
#Palíndromo. Um palíndromo é uma seqüência de caracteres
# cuja leitura é idêntica se feita da direita para esquerda ou vice−versa.
# Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
#---------------------------------------------------------------------------

sequence_caract = input("digite algo para saber se é palíndromo ou não: ")
sequence_caract = sequence_caract.replace(" ", "")

if sequence_caract[::-1] == sequence_caract:
    print("É palíndromo")
else:
    print("Não é palíndromo")