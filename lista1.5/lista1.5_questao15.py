# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Carlos Eduardo Tapudima de Oliveira       1715310030
# Frederico Victor Alfaia Rodrigues         1515200030
# Joelson Pereira Lima	                    1715310060
# Lucas Gabriel Silveira Duarte             1715310053
# Reinaldo da Silva Vargas	                1715310054
# Walter Nobre da Silva Conceição           1715310057
#
# 15 - João recebeu seu salário e precisa pagar duas contas que estão
# atrasadas, João terá de pagar multa de 2% sobre cada conta. Faça um programa
# que calcule e mostre quanto restará do salário de João.
# ----------------------------------------------------------

salary = float(input('Entre com seu salario: ')) # Recebe o salário
bill01 = float(input('Entre com o valor da primeira conta: ')) # Recebe o valor da primeira conta
bill02 = float(input('Entre com o valor da segunda conta: ')) # Recebe o valor da segunda conta
bill01 = bill01 * 1.2 # Aplica a multa de 2%
bill02 = bill02 * 1.2 # Aplica a multa de 2%
bills_acomulator = bill01+bill02 # Calcula o valor total das contas a pagar
remaining_salary = salary - bills_acomulator # Subtraiu o valor das contas do salário
print('O valor da primeira conta com 2% de multa é: ', bill01) # Mostra o valor da primeira conta com multa
print('O valor da segunda conta com 2% de multa é: ',bill02) # Mostra o valor da segunda conta com multa
print('O valor total de contas a pagar é: ',bills_acomulator) # Mostra o somatório das duas contas
print('O valor que resta do salário após o pagamento é: ', round(remaining_salary,2)) # Mostra o salário que sobra
