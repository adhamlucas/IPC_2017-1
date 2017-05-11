linhas = 16
colunas = 16
matriz = []
lista = 16*[None]


lista[0] = [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0]
lista[1] = [0,0,0,1,1,2,2,2,2,0,0,1,1,0,0,0]
lista[2] = [0,0,1,0,0,2,2,2,2,0,0,0,0,1,0,0]
lista[3] = [0,1,0,0,2,2,2,2,2,2,0,0,0,0,1,0]
lista[4] = [0,1,0,2,2,0,0,0,0,2,2,0,0,0,1,0]
lista[5] = [1,2,2,2,0,0,0,0,0,0,2,2,2,2,2,1]
lista[6] = [1,2,2,2,0,0,0,0,0,0,2,2,0,0,2,1]
lista[7] = [1,0,2,2,0,0,0,0,0,0,2,0,0,0,0,1]
lista[8] = [1,0,0,2,2,0,0,0,0,2,2,0,0,0,0,1]
lista[9] = [1,0,0,2,2,2,2,2,2,2,2,2,0,0,2,1]
lista[10] = [1,0,2,2,1,1,1,1,1,1,1,1,2,2,2,1]
lista[11] = [0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0]
lista[12] = [0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0]
lista[13] = [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0]
lista[14] = [0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0]
lista[15] = [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0]
print(lista)

for i in range(16):
    matriz.append(lista[i])

for element in matriz:
    print(*element)




#for i in range(linhas):
#    linha = []
#    for j in range(colunas):
#        valor = int(input('input a value[%d;%d]: ' %(i+1,j+1)))
#        linha.append(valor)
#    matriz.append(linha)
#
#for element in matriz:
#    print(*element)