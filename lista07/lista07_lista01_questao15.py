matriz = []
linha = []
somas = []
for i in range(3):
    for j in range(5):
        linha.append(input())
    matriz.append(linha)
    
for i in range(10):
    soma = 0
    for j in range(10):
        soma+=matriz[i][j]
    somas.append(soma)
print(somas)
