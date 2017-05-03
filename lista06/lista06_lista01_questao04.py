#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Nayara da Silva Cerdeira da Costa     1715310038
# Joelson Pereira Lima 			        1715310060
# Ian Gabriel Costa Machado             1215120276
#
#4.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
#----------------------------------------------------------------------------------------------------------------------
vetor = input().split()
consoantes = 0
for i in vetor:
    for letra in i:
        if letra not in ["a","e","i","o","u"]:
            consoantes +=1

print(consoantes)

