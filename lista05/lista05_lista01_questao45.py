# ---------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA  1515090555
# TIAGO FERREIRA ARANHA              1715310047
# VÍTOR SIMÕES AZEVEDO               1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA   1715310063
# REINALDO VARGAS                    1715310054
#
#45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
# aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
# nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
# aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#a. Maior e Menor Acerto;
#b. Total de Alunos que utilizaram o sistema;
#c. A Média das Notas da Turma.
#Gabarito da Prova:
#
#01 - A
#02 - B
#03 - C
#04 - D
#05 - E
#06 - E
#07 - D
#08 - C
#09 - B
#10 - A
#----------------------------------------------------------------------------------------------------------------------

students = int(input("Informe a quantidade de alunos que utilizarão o sistema: "))

c = 0
sum = 0
maiorAcerto = -1
menorAcerto = 11
soma_media = 0
final = 1

while final <= students:

    q1 = input("Informe sua resposta para a questão 1:")
    if q1 == "A" or q1 == "a":
        sum = sum + 1

    q2 = input("Informe sua resposta para a questão 2:")
    if q2 == "B" or q2 == "b":
        sum = sum + 1

    q3 = input("Informe sua resposta para a questão 3:")
    if q3 == "C" or q3 == "c":
        sum = sum + 1

    q4 = input("Informe sua resposta para a questão 4:")
    if q4 == "D" or q4 == "d":
        sum = sum + 1

    q5 = input("Informe sua resposta para a questão 5:")
    if q5 == "E" or q5 == "e":
        sum = sum + 1

    q6 = input("Informe sua resposta para a questão 6:")
    if q6 == "E" or q6 == "e":
        sum = sum + 1

    q7 = input("Informe sua resposta para a questão 7:")
    if q7 == "D" or q7 == "d":
        sum = sum + 1

    q8 = input("Informe sua resposta para a questão 8:")
    if q8 == "C" or q8 == "c":
        sum = sum + 1

    q9 = input("Informe sua resposta para a questão 9:")
    if q9 == "B" or q9 == "b":
        sum = sum + 1

    q10 = input("Informe sua resposta para a questão 10:")
    if q10  == "A" or q10 == "a":
        sum = sum + 1

    if sum > maiorAcerto:
        maiorAcerto = sum

    if sum < menorAcerto:
        menorAcerto = sum

    soma_media = float(soma_media + sum)
    print('-'*40)

    cond = int(input('Continua? (Y = 1/N = 0)'))
    if cond == 1:
            final += 1
    else:
        final = students
        break

print("O menor acerto foi =",menorAcerto)
print("O maior acerto foi = ",maiorAcerto)
print("O total de alunos que utilizaram o sistemas =",students)
print("A média de notas da turma foi =",soma_media)
