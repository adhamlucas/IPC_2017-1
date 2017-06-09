# --------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA  1515090555
# TIAGO FERREIRA ARANHA              1715310047
# VÍTOR SIMÕES AZEVEDO               1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA   1715310063
# REINALDO VARGAS                    1715310054
#
# 15. Escreva um algoritmo em PORTUGOL que receba oito números do usuário e imprima
# o logaritmo de cada um deles na base 10.
# --------------------------------------------------------------------------

import math

contador = 1

while c <= 8:
    numero = float(input("Número {}: ".format(c)))
    log = math.log10(numero)
    print("Logaritmo de %5.2f na base 10 é %5.2f" % (numero, log))
    contador += 1
