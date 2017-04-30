#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vet = []

for i in range (1,10):

    numbers = float(input())
    vet.append(numbers)

vet.reverse()
print(vet)


