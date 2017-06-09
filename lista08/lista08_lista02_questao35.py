def somar_linhas(matriz):

    somatoria = []

    for i in range (12):

        soma = 0

        for j in range (12):

            soma += A[i][j]

        somatoria.append(soma)

    return somatoria

A = []

for i in range (12):

    A.append([0]*12)

    for j in range (12):

        A[i][j] = int(input())

print(somar_linhas(A))