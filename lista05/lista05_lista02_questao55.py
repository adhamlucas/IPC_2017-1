# encoding: utf-8
# --------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA - 1515090555
# TIAGO FERREIRA ARANHA - 1715310047
# VÍTOR SIMÕES AZEVEDO - 1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA - 1715310063
# REINALDO VARGAS - 1715310054
#
# 55) Criar um algoritmo que leia o valor de N, imprima a seqüência a seguir e o resultado.
# N! / 0! – (N-1)! / 2! + (N-2)! / 4! – (N-3)! / 6! + ... 0! / (2N)!
# --------------------------------------------------------------------------

numero1 = int(input("Informe inteiro: "))

numero2 = 0
operacao = 1
resultado = 0
sequencia = ""

while numero1 >= 0:

    i = 1
    fatorial1 = 1
    while i <= numero1:
        fatorial1 = fatorial1 * i
        i += 1

    i = 1
    fatorial2 = 1
    while i <= numero2:
        fatorial2 = fatorial2 * i
        i += 1

    resultado = resultado + (fatorial1 / fatorial2) * operacao

    if operacao == 1:
        sequencia = sequencia + " + " + str(numero1) + "!/" + str(numero2) + "!"
    else:
        sequencia = sequencia + " - " + str(numero1) + "!/" + str(numero2) + "!"

    numero1 -= 1
    numero2 += 2
    operacao *= -1

print("Sequência: %s" % sequencia)
print("Resultado: %5.2f\n" % resultado)
