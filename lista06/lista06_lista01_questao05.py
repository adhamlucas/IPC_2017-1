#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 

count = 0
limit = 20
vet = []
vet_pair = []
vet_odd = []


while count < limit:
    number = int(input('Digite o número %d: ' % (count+1)))
    vet.append(number)
    count += 1

for element in vet:
    if element % 2 == 0:
        vet_pair.append(element)
    else:
        vet_odd.append(element)

print(vet)
print(vet_pair)
print(vet_odd)
