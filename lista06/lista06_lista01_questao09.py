#9)Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos
#do vetor.
#-----------------------------------------------------------------------------------------------------------------------

A = input().split()
size = int(len(A))
c = 0
soma = 0

while c < size:
    soma += (int(A[c]))**2
    c += 1
print(soma)
