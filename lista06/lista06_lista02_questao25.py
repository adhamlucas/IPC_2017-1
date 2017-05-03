#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# FANG YAO                                1115180236
# LUIZ PAULO MACHADO E SOUZA              1515200542
# FELIPE GUERREIRO DE MELLO               1315120052
# YURI LEANDRO DE AQUINO SILVA            1615100462
#
#25) Fazer um algoritmo em PORTUGOL que:
#a) Leia um conjunto de valores inteiros correspondentes a 80 notas dos alunos de uma
#turma, notas estas que variam de 0 a 10;
#b) Calcule a freqüência absoluta e a freqüência relativa de cada nota;
#c) Imprima uma tabela contendo os valores das notas (de 0 a 10) e suas respectivas
#freqüências absoluta e relativa.
#Observações:
#1. Freqüência absoluta de uma nota é o número de vezes em que aparece no conjunto de
#dados;
#2. Freqüência relativa é a freqüência absoluta divida pelo número total de dados;
#3. Utilizar como variável composta somente aquelas que forem necessárias.

list=[]
for i in range (0,80):
    n=float(input())
    if(n<0 or n>10 ):
        print("nota invalida")
        list.append(n=float(input()))
    else:
        list.append(n)
list_2=[]
for i in range (0,80):
    list_2.append(int(list.count(list[i])))
list_3=[]
for i in range (0,80):
    list_3.append(list_2[i]/10)
for i in range(0,80):
    print("Nota: ",list[i],"Frequência Absoluta: ",list_2[i],"Frequência Relativa: ",list_3[i])
