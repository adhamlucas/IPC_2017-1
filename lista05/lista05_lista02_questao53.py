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
# Implementar um algoritmo em PORTUGOL para calcular o cos(X). O valor de X
# deverá ser digitado em graus. O valor do cosseno de X será calculado pela soma dos
# 15 primeiros termos da série a seguir:
#
# cox = 1 - x**2 / 2! + x**4 / 4! - x**6 / 6! + x** / 8! - x**10 / 10! ...
# --------------------------------------------------------------------------

x = float(input("Informe o grau: "))
x = (x*3.1415926535)/180
c = 1
cosx = 0
m = 2

while c <= 14:
    i = 1
    fatorial = 1

    while i <= m:
        fatorial = fatorial * i
        i += 1
    cosx = cosx + (x ** m / fatorial) 
    c += 1
    m += 2
    cosx = -cosx
cosx = 1 - cosx

print(cosx)
