#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#Natália Cavalcante Xavier     1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Viniciius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514
#Lukas Michel Souza Mota 1715310018
#Seja a seguinte série:
#1, 4, 9, 16, 25, 36, ...
#Escreva um algoritmo que gere esta série até o N-ésimo termo. Este N-ésimo termo é digitado pelo usuário.
c=0
n=int(input("Digite o N-ésimo termo "))
while c<n:
    c=c+1
    termo=c**2
    print(termo)

