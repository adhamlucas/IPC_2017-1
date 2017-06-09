#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Natália Cavalcante Xavier              1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# dado a expressão da questão, escreva um algoritmo em Python que:
# a) Leia o valor de n, sendo n ? 20;
# b) Leia os coeficientes
# i a , i = 0, 1, 2 , ..., n;;
# c) Calcule o valor de P para 10 valores lidos para x;
# d) Imprima o valor de x e o valor de P correspondente.
#---------------------------------------------------------------------------

n = int(input())
termos = []
i = 0
c = 1
P = []
xis = []

while n <= 20:
    
    n = int(input("valor inválido, digite um número até 20: "))
    
while i < n:
    
    valor = float(input())
    termos.append(valor)
    i += 1
    
i = 0

while i < 10:
    
    x = int(input())
    xis.append(x)
    
    while c < n:
        
        resultado += (valor[n-c])*(x**(n-c))
        c += 1
        
    P.appedn(resultado)
    i += 1
    c = 1

i = 0

while i < 10:
    
    print ("para x =", xis[i], "temos como resultado =", P[i])
    i += 1
