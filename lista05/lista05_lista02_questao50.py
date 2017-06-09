# -----------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Gabriel Nascimento de Oliveira    1715310052
# Gabriel de Queiroz Souza          1715310044
# Guilherme Silva de Oliveira       1715310034
# Hugo Thadeu Silva Cardoso         1715310013
# Jandinne Duarte de Oliveira       1015070265
# Joelson Pereira Lima              1715310060
#
# Faça um algoritmo que:
# - leia um número real X do teclado;
# - determine e imprima o seguinte somatório:
# Usando os 20 primeiros termos da série.
# -----------------------------------------------------------------------------------------
num = float(input("Informe valor: "))
cont = 19
val = 1
fat = 1
aux = 1
soma = num
print("S = ", num, end="")
while cont > 0:
    while fat <= val:
        fat = fat * val
        val = val + 1
    if aux % 2 == 0:
        print(" + %.1f/%d!" % (num, aux), end="")
        soma = soma + (num / fat)
    else:
        print(" - %.1f/%d!" % (num, aux), end="")
        soma = soma - (num / fat)
    if cont == 1:
        print(" = %.2f" % (soma))
    aux = aux + 1
    val = 1
    fat = aux
    cont = cont - 1
    print("\n")
