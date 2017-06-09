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
# 14 - Faça um programa que receba o ano de nascimento de uma
# pessoa e o ano atual, calcule e mostre:
# a) a idade dessa pessoa em anos;
# b) a idade dessa pessoa em meses;
# c) a idade dessa pessoa em dias;
# d) a idade dessa pessoa em semanas;
# ----------------------------------------------------------

print ('---------------------Cálculo da Idade---------------------')
try:
    running_year = input ('Digite o ano atual: ')
    running_year = int(running_year)
    birth_year = input ('Digite o ano de nascimento: ')
    birth_year = int(birth_year)
    age = running_year - birth_year
    age_in_months = age * 12
    age_in_days = age * 365
    age_in_weeks = age * 48
    print (' A subtração',running_year,'  - ',birth_year,' é igual a : ',age,' que é a idade da pessoa em anos')
    print(' A multiplicação ',age,' * ',12,' é igual a : ',age_in_months,' que é a idade da pessoa em meses')
    print(' A multiplicação ',age,' * ',365,' é igual a : ',age_in_days,' que é a idade da pessoa em dias')
    print(' A multiplicação ',age,' * ',48,' é igual a: ',age_in_weeks,' que é a idade da pessoa em semanas')
except ValueError:
    print(' Somente números são aceitos, tente novamente!')
