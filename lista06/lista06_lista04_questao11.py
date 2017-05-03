#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Gabriel de Queiroz Sousa                1715310044
# Lucas Gabriel Silveira Duarte           1715310053
# Matheus de Oliveira Marques             1515310514
# Rodrigo Duarte de Souza                 1115140049
#
# Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador poderá errar 6 vezes antes de ser enforcado.
#---------------------------------------------------------------------------

import random
arq = open("forc.txt", "r")
texto = arq.readlines()
palavra = random.choice(texto)
print(palavra)
i = 1
erro = 0
cont = 0
frase = []
while i < len(palavra):
    frase.append("_")
    i+=1
print(*frase)
i = 0
tam = len(palavra)

while erro < 6:
    forc = input("Informe uma letra: ")
    while i < len(palavra):
        if forc == palavra[i]:
            frase[i] = forc
            i +=1
            cont = 1
            tam = tam - cont
        else:
            i +=1
    print(*frase)

    if cont == 0:
        erro +=1
        if erro < 6:
            print("Você errou pela %dª vez" % erro)
        else:
            print("Você errou pela 6ª vez. Perdeu!!")
    elif tam == 1:
        print("Parabéns você ganhou!! Frase = ", end="")
        print(*frase)
        exit(0)
    cont = 0
    i = 0