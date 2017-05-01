#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Gabriel de Queiroz Sousa                1715310044
# Lucas Gabriel Silveira Duarte           1715310053
# Matheus de Oliveira Marques             1515310514
# Rodrigo Duarte de Souza                 1115140049
#
#Número por extenso.
# Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
#---------------------------------------------------------------------------

units = ["zero", "um", "dois", "três", "quatro",
            "cinco", "seis", "sete", "oito", "nove"]

teens = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

dozens = ["dez", "vinte", "trinta", "quarenta", "cinquenta",
        "sessenta", "setenta", "oitenta", "noventa"]

number = input("digite um número para ser escrito por extenso: ")
number = number.zfill(3)
position_a = int(number[0])
position_b = int(number[1])
position_c = int(number[2])

if position_a == 0:
    if position_b == 0:
        resultado = units[position_c]
        print(resultado)
    elif position_b == 1:
        if position_c >= 0 and position_c <= 9 :
            resultado = teens[position_c]
            print(resultado)
    elif position_b == 2:
        if position_c == 0:
            resultado = dozens[position_b - 1]
            print(resultado)
        if position_c > 0 and position_c <= 9:
            resultado = "vinte e " + units[position_c]
            print(resultado)
    elif position_b >= 3 and position_b <= 9:
        if position_c == 0:
            resultado = dozens[position_b - 1]
            print(resultado)
        if position_c > 0 and position_c <= 9:
            resultado = dozens[position_b -1] + " e " + units[position_c]
            print(resultado)










