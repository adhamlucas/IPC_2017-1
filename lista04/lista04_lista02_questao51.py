#-----------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Adham Lucas da Silva Oliveira         1715310059
# Alexandre Marques Uchôa               1715310028
# André Luís Laborda Neves              1515070006
# Carlos Eduardo Tapudima de Oliveira	1715310030
# Diego Reis Figueira                   1515070169
#
# Leia um valor com duas casas decimais, equivalente ao salário
# de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor
# que esta pessoa deve pagar de Imposto de Renda,
# segundo a tabela abaixo:

# Renda                    Imposto
# de 0 a 2000,00           isento
# de 2001,00 a 3000,00     0,08
# de 3001,00 a 4500,00     0,18
# de 4500,00 par acima     0,28
#-----------------------------------------------------------------------------

salary = float(input())

if salary <= 2000:
    print('Isento')

if 2000.01 <= salary <= 3000:
    taxe = ((salary-2000)*0.08)
    print('R$ %.2f' % taxe)

if 3000.01 <= salary <= 4500:
    taxe = ((1000*0.08) + ((salary-3000)*0.18))
    print('R$ %.2f' % taxe)

if salary > 4500:
    taxe = ((1000*0.08) + (1500*0.18) + ((salary-4500)*0.28))
    print('R$ %.2f' % taxe)
