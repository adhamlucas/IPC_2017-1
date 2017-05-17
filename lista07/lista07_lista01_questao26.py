#calcular matriz transposta
tam = int(input('Informe tamanho da matriz quadrática: '))
matr = [[0 for z in range(tam)] for x in range(tam)]

for i in range(tam):
    for j in range(tam):
        matr[i][j] = int(input("Informe matriz %i%i: " % (i+1, j+1)))
print('Transposta:')
for i in range(tam):
    for j in range(tam):
        print(matr[j][i], end=" ")
    print()