#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#Natália Cavalcante Xavier     1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Viniciius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514
#Lukas Michel Souza Mota 1715310018

#Escreva  um  algoritmo para  calcular  o  fatorial do  número  N,  cujo 
#valor é obtido através do usuário pelo teclado
fat=int(input("Digite um valor "))
i=1
nfat=1
while i<=fat:
    nfat= nfat * i
    i= i + 1
print("%d!=%d"%(fat,nfat))
