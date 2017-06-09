#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Luiz Daniel Raposo Nunes de Mello 1715310049
# Kethelen Tamara Braga Barbosa     1525212002
# Luiz Paulo Machado e Souza        1515200542
# Lucas Gabriel Silveira Duarte     1715310053
# Luis Gustavo Moura de Queiros     1715310037
#
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.
#---------------------------------------------------------------------------

n = int(input("Digite o valor de n (n > 0): "))

é_primo = True

divisor = 2
while divisor < n and é_primo:
    if n % divisor == 0:
        é_primo = False
    divisor += 1

if é_primo and n != 1:
    print(n, "é primo")
else:
    print(n, "não é primo")
