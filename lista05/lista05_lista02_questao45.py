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
# 45) Seja a seguinte série:
# 1, 4, 4, 2, 5, 5, 3, 6, 6, 4, 7, 7, ...
# Escreva um algoritmo em PORTUGOL que seja capaz de gerar os N termos dessa
# série. Esse número N deve ser lido do teclado.
# ---------------------------------------------------------------------------
numero = int(input('Informe um número inteiro: '))
c = 1

while c <= numero:
    print(c, c + 3, c + 3)
    c = c + 1
