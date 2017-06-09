#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

#Carlos Eduardo Tapudima de Oliveira 1715310030
#Diogo Duarte  1715310056
#Dayana Picanço 1715310058
#Natalia Cavalcante  1715310021
#Walter Nobre da Silva Conceição 1715310057
#

from lista08.ipc import quantidade_de_pares
tamanho=int(input("Digite o tamanho do vetor "))
vet = []
for i in range(1,tamanho+1):
    valor = int(input("Digite um valor "))
    vet.append(valor)
cont = quantidade_de_pares(vet)
print(cont)
