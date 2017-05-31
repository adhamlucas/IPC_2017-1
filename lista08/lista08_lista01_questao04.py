#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Gabriel de Queiroz Sousa                  1715310044
# Lucas Gabriel Silveira Duarte             1715310053
#
# Faça um programa, com uma função que necessite de um argumento. 
#A função retorna o valor de caractere ‘P’, se seu argumento for positivo, 
#e ‘N’, se seu argumento for zero ou negativo.
#----------------------------------------------------------------------------------------------------------------------
number = int(input("digite um número: "))

def arg_porn(number):
    if number > 0 and number != 0:
        number = "P"
    else:
        number = "N"
    return number

print(arg_porn(number))
