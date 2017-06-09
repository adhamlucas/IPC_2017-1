#-----------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Kethelen Tamara Braga Barbosa           1525212002
# Lucas Gabriel Silveira Duarte           1715310053
# Luis Gustavo Moura de Queiroz           1715310037
# Luiz Daniel Raposo Nunes de Mello       1715310049
# Luiz Paulo Machado e Souza              1515200542
#
# Faça um programa que peça dois números, base e expoente,
# calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
#-----------------------------------------------------------------------------------------------------------------

number1 = int(input("digite um número que servirá de base:"))
number2 = int(input("digite um número que servirá de expoente: "))
counter = 1
number = number1

while counter < number2:
    number = number * number1
    counter += 1

print("o número",number1,"elevado ao número",number2,"é:",number)
