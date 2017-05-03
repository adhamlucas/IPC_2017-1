#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# FANG YAO                                1115180236
# LUIZ PAULO MACHADO E SOUZA              1515200542
# FELIPE GUERREIRO DE MELLO               1315120052
# YURI LEANDRO DE AQUINO SILVA            1615100462  
#
# 14) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
#-----------------------------------------------------------------------------------------------------------------------

lista = ["Telefonou para a vítima?:", "Esteve no local do crime?:", "mora perto da vítima?:",
         "Devia para a vítima?:", "Já trabalhou com a vítima?:"]
size = int(len(lista))
sim = 0
c = 0

while c < size:
    resposta = input(lista[c])
    if resposta == "sim":
        sim += 1
    c += 1
if sim < 2:
    print("voce é o inocente!")
elif sim >= 2:
    print("voce é o suspeito!")
elif 4<= sim < 5:
    print("voce é o cumplice!")
elif sim == 5:
    print("voce é o assassino!!")
