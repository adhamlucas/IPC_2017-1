#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

#Reinaldo da Silva Varas 1715310054
#Natalia Cavalcante Xavier 1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Vinicius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514
#Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, 
#ao utilizar um automóvel que faz 12 KM/L.
#Para isso, ele gostaria que você o auxiliasse através de um simples programa.
#Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h)
#Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários.
#Mostre o valor com 3 casas decimais após o pont
#-------------------------------------------------------------------------------------

timetrip = float(input("Informe o tempo de viagem: "))
speed = float(input("Informe a velocidade: "))
distance = speed*timetrip
liters = distance/12
print("São necessarios %.3f " %liters,"litros")
