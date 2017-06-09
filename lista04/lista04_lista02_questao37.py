#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

#Reinaldo da Silva Vargas 1715310054
#Natalia Cavalcante Xavier 1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Vinicius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514

#Você deve fazer um programa que lê um número de ponto flutuante e imprima uma mensagem dizendo em qual dos seguintes
##  intervalos o número pertence: [0,25] (25,50], (50,75], (75,100). Número for menor que zero ou superior a 100,
# o programa deve imprimir a mensagem "Fora de intervalo" que significa "Fora de Intervalo".

#O símbolo '(' representa mais grande do que, por exemplo:
#[0,25] indica números entre 0 e 25,0000, incluindo ambos.
#(25, 50) indica números maiores que 25 (25.00001) até 50.0000.000.
#Entrada

#O arquivo de entrada contém um número de ponto flutuante.
#Saída

#A saída deve ser uma mensagem como exemplo a seguir.
#Amostra de entrada
#Amostra de saída

#25, 01           Intervalo(25, 50)

#25, 00           Intervalo[0, 25]

#100, 00          Intervalo(75, 100)

#-25, 02           Fora de intervalo
#------------------------------------------------------------------------------

number = float(input())

if 0 <= number <= 25:
    print("Intervalo [0,25]")
elif 25 < number <= 50:
    print("Intervalo (25,50]")
elif 50 < number <= 75:
    print("Intervalo (50,75]")
elif 75 < number <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")

