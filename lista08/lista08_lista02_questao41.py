def media_diagonal_principal (matriz):

    menor = matriz[1][6]

    for i in range (7):

        for j in range (7):

            if j + i >= 7:

                if matriz[i][j] < menor:
                    
                    menor = matriz[i][j]

    return menor

A = []

for i in range (7):

    A.append([0] * 7)

    for j in range (7):

        A[i][j] = int(input())

print(media_diagonal_principal(A))