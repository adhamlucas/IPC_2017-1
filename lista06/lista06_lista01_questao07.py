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
#7.Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números
#----------------------------------------------------------------------------------------------------------------------
vetor = input("digite 5 números:")
vetor = vetor.split()
c = 0
soma =0
multi = 1

while c < 5:
    soma += int(vetor[c])
    multi *= int(vetor[c])
    c += 1
print("soma: ",soma)
print("multiplicação: ",multi)
print(vetor[:5])