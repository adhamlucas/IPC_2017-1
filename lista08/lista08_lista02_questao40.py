def media_diagonal_principal (matriz):

    media = 0

    for i in range (10):

        for j in range (10):

            if j > i:

                media += matriz[i][j]

    return media

A = []

for i in range (10):

    A.append([0] * 10)

    for j in range (10):

        A[i][j] = int(input())

print(media_diagonal_principal(A))