#---------------------------------------------------------------------------
# Introdu��o a Programa��o de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Nat�lia Cavalcante Xavier              1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# Dado um conjunto de 100 valores num�ricos dispon�veis num meio de entrada
# qualquer, fazer um algoritmo em PORTUGOL para armazen�-los numa vari�vel
# composta B, e calcular e imprimir o valor do somat�rio dado pela quest�o
#---------------------------------------------------------------------------

i = 0
valores = []
soma = 0

while i < 100:

    valor = float(int())
    valores.append(valor)
    i += 1
    
i = 0

while i < 50:

    soma = valores[i] + valores[99-i]
    i += 1
    
print(soma)
