matriz = []
linha = []

for i in range(10):
    for j in range(10):
        linha.append(input())
    matriz.append(linha)
    
for i in range(10):
    for j in range(10):
        if j > i:
            print (matriz[i][j])
