#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

#Reinaldo da Silva Varas 1715310054
#Natalia Cavalcante Xavier 1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Vinicius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514

#Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por
# aluno e apresentar:
#
#   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#  A mensagem "Reprovado", se a média for menor do que sete;
#  A mensagem "Aprovado com Distinção", se a média for igual a dez.
#------------------------------------------------------------------------------


note1 = float(input("Informe primeira nota parcial: "))
note2 = float(input("Informe segunda nota parcial: "))

average = (note1 + note2)/2

if average >= 7:
    print("Aprovado")
elif average <7:
    print("Reprovado")
elif average == 10:
    print ("Aprovado com Distinção")
