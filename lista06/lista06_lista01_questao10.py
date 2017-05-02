#10)Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
#deverão ser compostos pelos elementos intercalados dos dois outros vetores.
#-----------------------------------------------------------------------------------------------------------------------

vetorA = input().split()
size = int(len(vetorA))
vetorB = input().split()
vetorC = []
c = 0
while c < size:
    vetorC.append(vetorA[c])
    vetorC.append(vetorB[c])
    c += 1
print(vetorC)
