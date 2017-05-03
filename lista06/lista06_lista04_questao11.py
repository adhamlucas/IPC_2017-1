# ---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Natália Cavalcantre Xavier              1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# Lista 4. Q 11 Jogo de Forca. Desenvolva um jogo da forca.
#           O programa terá uma lista de palavras lidas de
#           um arquivo texto e escolherá uma aleatoriamente.
#           O jogador poderá errar 6 vezes antes de ser enforcado.
# ----------------------------------------------------------------------------

import random

palavras = ['vaca', 'coelho', 'sapo']

palavra = random.choice(palavras)

erro = 0
acerto = -1
errado = 0
forca = []
for i in palavra:
    forca.append("_")

print(palavra)

while erro <= 6:

    if errado > 0 and acerto == 0:
        print("Você errou pela %dª vez. Tente de novo!" % errado)
    letra_teste = input("\nDigite uma letra: ")
    acerto = 0
    for i, letra in enumerate(palavra):
        if letra_teste == letra and letra != "_":
            forca[i] = letra_teste
            acerto += 1


    if acerto > 0:
        errado += 1

    erro += 1

    print("A palavra é: ", end='')
    for i in forca:
        print(i, end=' ')

if erro <= 6:
    print("Você ganhou!")
