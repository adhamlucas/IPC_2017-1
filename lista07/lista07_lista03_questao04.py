#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Diogo Duarte  1715310056
# Dayana Picanço 1715310058
# Walter Nobre 1715310057
matriz = []
for i in range(3):
    for j in range(3):
        linha.append(i+j)
    matriz.append(linha)
cont = 0
c = '.'
flag while flag and cont<9:
    x = int(input("cordenada x: "))
    y = int(input("cordenada y: "))
    matriz[y][x] = 'x'
    if(matriz[0][0]==matriz[0][1]==matriz[0][1]):
        flag = 0
        c = matriz[y][x]
    if(matriz[1][0]==matriz[1][1]==matriz[1][1]):
        flag = 0
        c = matriz[y][x]
    if(matriz[2][0]==matriz[2][1]==matriz[2][2]):
        flag = 0
        c = matriz[y][x]
        
    if(matriz[0][0]==matriz[1][0]==matriz[2][0]):
        flag = 0
        c = matriz[y][x]
    if(matriz[0][1]==matriz[1][1]==matriz[2][1]):
        flag = 0
        c = matriz[y][x]
    if(matriz[0][2]==matriz[1][2]==matriz[2][2]):
        flag = 0
        c = matriz[y][x]
        
    if(matriz[0][0]==matriz[1][1]==matriz[2][2]):
        flag = 0
        c = matriz[y][x]
    if(matriz[2][0]==matriz[1][1]==matriz[0][2]):
        flag = 0
        c = matriz[y][x]
    cont+=1
if c == '.':
    print("velha")
else if c=='x':
    print("x ganhou")
else:
    print("o ganhpou")
