# ----------------------------------------------------------
# Introducao a Programacao de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Lukas Michel Souza Mota               1715310018
# Marcus Vinicius Paes da Silva Santos  1515070060
# Matheus de Oliveira Marques           1515310514
# Natalia Cavalcante Xavier             1715310021
# Nayara da Silva Cerdeira da Costa     1715310038
#
# Altere o programa de calculo dos numeros primos, 
# informando, caso o numero nao seja primo, por quais numero ele eh divisivel.
#----------------------------------------------------------

number = int(input('Digite um número: '))
count = 1
total_zero = 0
count2 = 1

while count <= number:
    primo = number % count
    count += 1
    if primo == 0:
        total_zero += 1

if total_zero > 2:
    print('O valor não é primo!')
    while count2 <= number:
        prime2 = number % count2
        divisibles = count2
        count2 += 1
        if prime2 == 0:
            print('Divisivel por:', divisibles)
else:
    print('O valor é primo!')
