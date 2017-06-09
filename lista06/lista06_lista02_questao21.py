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
#  Em uma cidade do interior, sabe-se que, de janeiro a abril de 1976 (121 dias), n�o
# ocorreu temperatura inferior a 15�C nem superior a 40�C. As temperaturas verificadas
# em cada dia est�o dispon�veis em uma unidade de entrada de dados.
# Fazer um algoritmo em PORTUGOL que calcule e imprima:
# - A menor temperatura ocorrida;
# - A maior temperatura ocorrida;
# - A temperatura m�dia;
# - O n�mero de dias nos quais a temperatura foi inferior � temperatura m�dia
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
print("temperatura m�dia:", media)
print("n� de dias de temperatura menor que a m�dia:", tempinf)
