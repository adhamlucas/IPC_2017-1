#11)Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
#-----------------------------------------------------------------------------------------------------------------------

vetorA = input().split()
size = int(len(vetorA))
vetorB = input().split()
vetorC = input().split()
vetorD = []
c = 0
while c < size:
    vetorD.append(vetorA[c])
    vetorD.append(vetorB[c])
    vetorD.append(vetorC[c])
    c += 1
print(vetorD)
