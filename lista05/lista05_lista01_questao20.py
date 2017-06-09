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
# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o 
# fatorial várias vezes e limitando o fatorial números inteiros positivos e menores que 16.
# -----------------------------------------------------------------------------------------

fat_value = int(input('Digite o número do fatorial: '))
count = 1
term = 1

while fat_value < 0 or fat_value >= 16:
    print('Error: fatorial negativo ou maior que 16')
    fat_value = int(input('Digite o número do fatorial: '))

while count <= fat_value:
    fatorial = count * term
    term = fatorial
    count += 1
    if count > fat_value:
        print('%.d! = %.d' % (fat_value, fatorial))
        next = input('Deseja continuar? (Y/N)')
        if next == 'Y' or next == 'y':
            fat_value = int(input('Digite o número do fatorial: '))
            while fat_value < 0 or fat_value >= 16:
                print('Error: fatorial negativo ou maior que 16')
                fat_value = int(input('Digite o número do fatorial: '))
            count = 1
            term = 1
