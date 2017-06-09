#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Diogo Roberto Duarte da Costa     1715310056
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro de Mello         1315120052
# Frederico Victor Alfaia Rodrigues 1515200030
# Gabriel Barroso da Silva Lima     1715310011
#
# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
# usuário o valor do saque e depois informar quantas notas de cada valor serão
# fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
# mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar
# com a quantidade de notas existentes na máquina.
#
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
# uma nota de 50, uma nota de 5 e uma nota de 1;
#
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
#  ----------------------------------------------------------

# Parâmetros inicias para o funcionamento do código
sake = int(input("Digite o valor do saque: "))
rest100 = sake % 100
rest50 = rest100 % 50
rest10 = rest50 % 10
rest5 = rest10 % 5
rest1 = rest5 % 1

if 600 >= sake >= 10:
    if rest100 > 0 or sake % 100 == 0:
        multiple100 = (sake - rest100)
        number_notes100 = (multiple100/100)
        print("quantidade de notas de 100 foi: ", number_notes100)
    if rest50 > 0 or sake % 50 == 0:
        multiple50 = (rest100 - rest50)
        number_notes50 = (multiple50/50)
        print("quantidade de notas de 50 foi: ", number_notes50)
    if rest10 > 0 or sake % 10 == 0:
        multiple10 = (rest50 - rest10)
        number_notes10 = (multiple10/10)
        print("quantidade de notas de 10 foi: ", number_notes10)
    if rest5 > 0 or sake % 5 == 0:
        multiple5 = (rest10 - rest5)
        number_notes5 = (multiple5/5)
        print("quantidade de notas de 5 foi: ", number_notes5)
    if rest1 > 0 or sake % 1 == 0:
        multiple5 = (rest5 - rest1)
        number_notes1 = (multiple5/1)
        print("quantidade de notas de 1 foi: ", number_notes1)
else:
    print("O valor digitado não é aceito para saque")
