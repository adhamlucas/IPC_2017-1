#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Dayana Picanço Marquez            1715310058
# Vitor Simões Azevedo              1715310025
# Wilbert Luís Evangelista Marins   1715310055
# Enrique Leão Barbosa Izel         1715310048
# Edson de Lima Barros              1715310043
# Víctor Hugo de Oliveira Carreira  1715310063
#
# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima
# o número de alunos com média maior ou igual a 7.0.
#---------------------------------------------------------------------------
c = 0
vetormedia = []
while c < 10:
    print("insira as 4 notas do aluno numero",c + 1)
    c2 = 0
    soma = 0
    while c2 < 4:
        notas = input("digite sua nota: ")
        soma = soma + float(notas)
        c2 = c2 + 1
    media = soma/4
    vetormedia.append(media)
    c = c + 1
    print("\n\n")
soma_alunos = 0
count = 1
while count < len(vetormedia):
    i = int(vetormedia[count])
    if i >= 7.0:
        soma_alunos = soma_alunos + 1
    count = count + 1
print("o numero de alunos com media maior ou igual a 7.0 é: ", soma_alunos)
