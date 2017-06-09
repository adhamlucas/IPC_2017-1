#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009 
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030 
# Felipe Eduardo Silva de Almeida   1715310031 
# Felipe Guerreiro De Mello         1315120052 
# Silas castro de Mendonça          1715310066
# 35.Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista
# dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

lim = int(input())
c = 3
div = 2

print("Numeros primos:")

if lim > 2:
    print("2")

while c<lim:

    if c % 2 == 0:
        c += 1

    else:

        if c == div:
            print(c)
            c += 1
            div = 2

        else:

            if c % div == 0:
                c += 1
                div = 2

            else:
                div += 1
