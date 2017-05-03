#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Antônio Diego Furtado da Silva         1715310004
# Aracille de Souza Barbosa              1315120206
# Marcus Vinicius Paes da Silva Santos   1515070060
# Silas Castro de Mendonça               1715310066
# Wesley da Silva Rocha                  1715310026
#
#Escreva um algoritmo em python que receba oito números do usuário e
# armazene em um vetor o logaritmo de cada um deles na base 10. Caso não seja
# possível calcular o valor para o número digitado, o número –1 deve ser atribuído ao
# elemento do vetor. Após isso, o algoritmo deve imprimir todos os valores
# armazenados.

#---------------------------------------------------------------------------

list =[]
limit = 8
count = 0

while count < limit:
    number = int(input("digite um número "))
    if number%10 == 0:
        number = number
    else:
        number = -1
    list.append(number)
    count += 1

print(list)