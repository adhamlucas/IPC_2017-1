#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Yuri Leandro de Aquino Silva - 1615100462
# Hugo Thadeu Silva Cardoso - 1715310013
# Wilbert Luís Evangelista Marins - 1715310055
# Enrique Leão Barbosa Izel - 1715310048
# Victor Summer Oliveira Pantaleao - 1715310042
#
# 4.  Dada uma matriz real  Amxn, verificar se existem elementos repetidos em A.
#
linhas=int(input())
colunas=int(input())
matriz=[]
for m in range(colunas):
    linha=[]
    for n in range(linhas):
        linha.append(input())
    matriz.append(linha)
list = []
verif = 0
while(verif != 1 ):
    for m in range(0,colunas):
        for n in range(0,linhas):
            if(matriz[m][n] in list):
                verif = 1
            else:
                list.append(matriz[n][m])
if(verif == 1):
    print("Há elemento repetido")