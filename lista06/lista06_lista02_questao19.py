#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Ulisses Antonio Antonino da Costa 1515090555
# Walter Nobre da Silva conceição 1715310057
# Jandinne Duarte de Oliveira 1015070265
# Vitor Summer Oliveira Pantaleão 1715310042
# Reinaldo vargas 1715310054
#
# 19) Escreva um algoritmo em PORTUGOL, que leia um conjunto de 50 fichas
# correspondente à alunos e armazene-as em vetores, cada uma contendo, a altura e o
# código do sexo de uma pessoa (código = 1 se for masculino e 2 se for feminino), e
# calcule e imprima:
# - A maior e a menor altura da turma;
# - As mulheres com altura acima da média da altura das mulheres;
# - As pessoas com altura abaixo da média da turma.

mht = 0      #SOMA DAS ALTURAS DA TURMA
msf = 0     #SOMA DA ALTURA DAS MULHERES DA TURMA
c = 0         #CONTADOR AUXILIAR PARA SABER QUAL MULHER ESTÁ ACIMA DA MÉDIA DAS MULHERES
height_list = []    #LISTA DAS ALTURAS
sex_list = []       #LISTA DO SEXO
for i in range(50):
    height = float(input("Altura: "))
    sex = int(input("Sexo: "))
    height_list.append(height)
    sex_list.append(sex)
print("menor altura é: %0.2f" %min(height_list))
print("maior altura é: %0.2f" %max(height_list))
for j in range(len(sex_list)):
    mht = height_list[j] + mht
    if sex_list[j] == 2:
        msf = height_list[j] + msf
        c = c + 1
t_s_l = len(height_list)        #TAMANHO DA LISTA DE SEXO
media_t = mht/t_s_l             #MEDIA TURMA (TAMANHO DA LISTA DE SEXO = TAMANHO DA LISTA DE ALTURA)... t_s_l
media_f = msf/c                 #MEDIA MULHERES
for a in range(len(height_list)):
    if sex_list[a] == 2:
        if height_list[a]>media_f:      #<<<<<<SABER QUAL MULHER ESTÁ ACIMA DA MÉDIA DAS MULHERES
            print("mulher(%d) está acima da média das mulheres: "%a , height_list[a])
    if height_list[a]<=media_t:         #<<<<<<<SABER QUAL PESSOA ESTÁ ACIMA DA MÉDIA
        print("pessoa(%d) abaixo da média da turma: " %a, height_list[a])
