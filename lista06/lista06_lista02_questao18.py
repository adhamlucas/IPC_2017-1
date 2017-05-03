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
# Implementar um algoritmo em Python para calcular o sen(X). O valor de X
# deverá ser digitado em graus. O valor do seno de X será calculado pela soma dos 15
# primeiros termos da série determinado na questão
# Esses termos devem ser armazenados em um vetor de reais.
#---------------------------------------------------------------------------

X = float(input())
i = 0
expoente = 1
fatorial = 1
divisor = 1
termos = []

while i < 15:
    
    while fatorial <= expoente:
        
        divisor *= fatorial
        fatorial += 1
    
    if i % 2 == 0:
        
        termo = (X**expoente)/divisor
        termos.append(termo)
    
    else:
        
        termo = -((X**expoente)/divisor)
        termos.append(termo)
        
    expoente += 2
    fatorial = 1
    divisor = 1
    i += 1
