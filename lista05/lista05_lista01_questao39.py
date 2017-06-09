# encoding: utf-8
#--------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA - 1515090555
# TIAGO FERREIRA ARANHA - 1715310047
# VÍTOR SIMÕES AZEVEDO - 1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA - 1715310063
# REINALDO VARGAS - 1715310054
#
# 39. Faça um programa que leia dez conjuntos de dois valores,
# o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros.
# Encontre o aluno mais alto e o mais baixo.
# Mostre o número do aluno mais alto e o número do
# aluno mais baixo, junto com suas alturas.
#--------------------------------------------------------------------------

c = 1

aluno_mais_alto = ""
aluno_mais_alto_altura = 0

aluno_mais_baixo = ""
aluno_mais_baixo_altura = 0

while c <= 10:
    aluno_nome = input("Informe o nome do aluno: ")
    aluno_altura = int(input("Informe a altura do aluno: "))

    if c == 1:
        aluno_mais_alto_altura = aluno_altura
        aluno_mais_baixo_altura = aluno_altura
        aluno_mais_alto = aluno_nome
        aluno_mais_baixo = aluno_nome
    else:
        if aluno_altura > aluno_mais_alto_altura:
            aluno_mais_alto_altura = aluno_altura
            aluno_mais_alto = aluno_nome
        elif aluno_altura < aluno_mais_baixo_altura:
            aluno_mais_baixo_altura = aluno_altura
            aluno_mais_baixo = aluno_nome
    c = c + 1

print("O aluno mais alto é %s e mede %5.2f" % (aluno_mais_alto, aluno_mais_alto_altura))
print("O aluno mais baixo é %s e mede %5.2f" % (aluno_mais_baixo, aluno_mais_baixo_altura))
