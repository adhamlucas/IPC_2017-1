# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Aracille de Souza Barbosa           1315120206
# Felipe Eduardo Silva de Almeida     1715310031
# Kethelen Tamara Braga               1525212002
# Nayara da Silva Cedeira da Costa    1715310038
# Vitor Summer Oliveira Pantaleão     1715310042
# Yuri Leandro de Aquino Silva        1615100462
#
# Faça um programa que calcule e mostre a tabuada de
# um número digitado pelo usuário
# ----------------------------------------------------------

tab=input("Qual a tabuada que você quer?")
num=int(input("De quanto?"))
if((tab=="x")or(tab=="vezes")):
    for x in range(11):
        resp=num*x
        print(resp)
elif((tab=="-")or(tab=="menos")):
    for x in range(11):
        resp=num-x
        print(resp)
elif((tab=="+")or(tab=="mais")):
    for x in range(11):
        resp=num+x
        print(resp)
else:
    for x in range(1,9):
        resp=num/x
        print(resp)
