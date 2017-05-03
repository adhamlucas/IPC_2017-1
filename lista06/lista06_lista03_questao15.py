#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Antônio Diego Furtado da Silva         1715310004
# Aracille de Souza Barbosa              1315120206
# Marcus Vinicius Paes da Silva Santos   1515070060
# Silas Castro de Mendonça               1715310066
# Wesley da Silva Rocha                  1715310026
#
#Em uma classe há n alunos, cada um dos quais realizou k provas com pesos distintos.
#Dados n , k, os pesos das k provas e as notas de cada aluno, calcular a média ponderada das 
#provas para cada aluno e a média aritmética da classe em cada uma das provas.
#
l=[]
notas=[]

media_pond = 0

count1 = 0
count2 = 0
count3 = 0

nota = 0
peso = 0
soma_peso=0

num_de_alunos= int(input("num_de_alunos: "))
num_de_provas= int(input("num_de_provas: "))

for i in range(num_de_alunos):


    count1 = media_pond + count1
    for j in range(num_de_provas):
        nota = float(input("nota: "))
        peso = int(input("peso: "))
        notas.append(nota)
        l.append(nota*peso)
        soma_peso = peso + soma_peso
        count2 = nota + count2
        count3 = nota * peso + count3
    media_pond = (count3)/soma_peso
    i +=1
    print("aluno(%d)" % i, "media ponderada->", media_pond)
    mediaar=(count2/num_de_provas)/num_de_alunos
print("Média A. é: %0.2f" %mediaar)
