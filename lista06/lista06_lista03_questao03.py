#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# FANG YAO                                1115180236
# LUIZ PAULO MACHADO E SOUZA              1515200542
# FELIPE GUERREIRO DE MELLO               1315120052
# YURI LEANDRO DE AQUINO SILVA            1615100462
#
#3.  Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o lançou n vezes.
# Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face.

b=int(input())
list=[]
for i in range (0,b):
    a=int(input())
    if(a < 0):
        list.append(a=int(input()))
    else:
        list.append(a)
list_2=[]
for i in range (0,b):
    list_2.append(int(list.count(list[i])))
for i in range(0,b):
    print("Lado: ",list[i],"Frequência : ",list_2[i])
