taml = 61
tamc = 10

mat = [[0 for x in range(tamc)] for z in range(taml)]
print(mat)

def pega_valores(mat):
    for i in range(taml-1):
        for j in range(tamc):
            mat[i][j] = int(input('Matriz %i %i: ' % (i+1, j+1)))
    return mat

def soma_valores(mat):
    for i in range(taml-1):
        for j in range(tamc):
            mat[taml-1][j] = mat[taml-1][j] + mat[i][j]
    return mat

def imprime_valores(x, y, mat):
    return mat[x][y]

m = pega_valores(mat)
m = soma_valores(m)
print('Matriz Alterada = ')

for i in range(taml):
    for j in range(tamc):
        print(imprime_valores(i, j, mat), end=' ')
    print()