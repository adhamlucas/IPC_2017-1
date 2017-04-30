#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 
vet = []
vet_pair = []
vet_odd = []

for i in range (0,20):

    number = int(input())
    vet.append(number)

    if number % 2 == 0 :
        vet_pair.append(number)

    else:
        vet_odd.append(number)

print(vet)
print(vet_pair)
print(vet_odd)
