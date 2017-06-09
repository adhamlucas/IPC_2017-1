#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009 
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030 
# Felipe Eduardo Silva de Almeida   1715310031 
# Felipe Guerreiro De Mello         1315120052 
# Silas castro de Mendonça          1715310066
#
#27.Faça um programa que calcule o número médio de alunos por turma. 
#Para isto, peça a quantidade de turmas e a quantidade de alunos
# para cada turma. As turmas não podem ter mais de 40 alunos. 
#----------------------------------------------------------------

classes = int(input("Informe o número de turmas "))

c = 0
sum = 0

while c < classes:
    students = int(input("Quantidades de alunos da turma: "))
    if students <= 40:
        sum = sum + students
        c = c + 1
    else:
        print("As turmas não podem ter mais de 40 alunos!")

average = sum/ c

print("A média de alunos por tuma é = ",int(average))
