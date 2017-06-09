#----------------------------------------------------------------------------------------------------------------------#
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
#
# Adham Lucas da Silva Oliveira         1715310059
# Alexandre Marques Uchôa               1715310028
# André Luís Laborda Neves              1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Diego Reis Figueira                   1515070169
#
# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule
#o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100,50,20,
#10,5,2.As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
#----------------------------------------------------------------------------------------------------------------------#
money = float(input())

if 0 <= money <= 1000000.00:
  one_hundred_reals = money//100
  money = money - (one_hundred_reals * 100)

  fifty_reals = money//50
  money = money - (fifty_reals * 50)

  twent_reals = money//20
  money = money - (twent_reals * 20)

  ten_reals = money//10
  money = money - (ten_reals * 10)

  five_reals = money//5
  money = money - (five_reals *5)

  two_reals = money//2
  money = money - (two_reals * 2)

  one_real = money//1
  money = money - (one_real * 1)

  fifty_cents = money//0.50
  money = money - (fifty_cents * 0.50)

  twenty_five_cents = money//0.25
  money = money - (twenty_five_cents * 0.25)

  ten_cents = money//0.10
  money = money - (ten_cents * 0.10)

  five_cents = money//0.05
  money = money - (five_cents * 0.05)

  one_cent = money//0.01
  money = money - (one_cent * 0.01)

print('NOTAS:')
print('%.0f nota(s) de R$ 100.00' % one_hundred_reals)
print('%.0f nota(s) de R$ 50.00' % fifty_reals)
print('%.0f nota(s) de R$ 20.00' % twent_reals)
print('%.0f nota(s) de R$ 10.00' % ten_reals)
print('%.0f nota(s) de R$ 5.00' % five_reals)
print('%.0f nota(s) de R$ 2.00' % two_reals)
print('MOEDAS:')
print('%.0f moeda(s) de R$ 1.00' % one_real)
print('%.0f moeda(s) de R$ 0.50' % fifty_cents)
print('%.0f moeda(s) de R$ 0.25' % twenty_five_cents)
print('%.0f moeda(s) de R$ 0.10' % ten_cents)
print('%.0f moeda(s) de R$ 0.05' % five_cents)
print('%.0f moeda(s) de R$ 0.01' % one_cent)



