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
#  Em uma cidade do interior, sabe-se que, de janeiro a abril de 1976 (121 dias), não
# ocorreu temperatura inferior a 15ºC nem superior a 40ºC. As temperaturas verificadas
# em cada dia estão disponíveis em uma unidade de entrada de dados.
# Fazer um algoritmo em PORTUGOL que calcule e imprima:
# - A menor temperatura ocorrida;
# - A maior temperatura ocorrida;
# - A temperatura média;
# - O número de dias nos quais a temperatura foi inferior à temperatura média
#---------------------------------------------------------------------------

i = 0
temperatura = []
tempinf = 0
media = 0
menor = 0
maior = 0

while i < 121:
    
    tempdia = float(input())
    temperatura.append(tempdia)
    media += tempdia
    
    if tempdia < menor:
        
        menor = tempdia
        
    if tempdia > maior:
        
        maior = tempdia
        
    i += 1
    
media /= 121
i = 0

while i < 121:
    
    if media < temperatura[i]:
        
        tempinf += 1
        
    i += 1
        
print("menor temperatura ocorrida:", maior)
print("maior temperatura ocorrida:", menor)
print("temperatura média:", media)
print("nº de dias de temperatura menor que a média:", tempinf)
