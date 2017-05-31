#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Gabriel de Queiroz Sousa                  1715310044
# Lucas Gabriel Silveira Duarte             1715310053
#
# Faça uma função que informe a quantidade de dígitos de um determinado 
#número inteiro informado. 
#----------------------------------------------------------------------------------------------------------------------


number = int(input("digite um número para saber quantos dígitos ele possui: "))

def qnt_digitos(number):
    number = str(number)
    number = len(number)
    return number

print("o número digitado possui:",qnt_digitos(number),"digitos")
