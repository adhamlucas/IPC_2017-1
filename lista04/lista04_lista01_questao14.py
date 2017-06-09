#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

#Reinaldo da Silva Varas 1715310054
#Natalia Cavalcante Xavier 1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Vinicius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514
#-------------------------------------------

number1 = float(input("Digite sua primeira nota "))
number2 = float(input("Digite sua segunda nota  "))
media = (n1+n2)/2

if media >9 and media < 10:
    print("Aprovado,conceito A")
if media > 7.5 and media < 9:
    print("Aprovado,conceito B")
if media > 6 and media < 7.5:
    print("Aprovado,conceito C")
if media > 4 and media < 6:
    print("Reprovado,conceito D")
if media > 0 and media < 4:
    print("Reprovado,conceito E")

print("Sua primeira nota foi ",number1)
print("Sua segunda nota foi ",number2)
print("Sua media foi ",media)
