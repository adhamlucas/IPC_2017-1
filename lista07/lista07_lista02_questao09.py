#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros   1715310043
# Tiago Ferreira Aranha  1715310047
# Vitor Simôes Azevedo   1715310025
# Lista2. Questão 9: Um jogo de palavras cruzadas pode ser representado por uma matriz  Amxn  onde cada posição da matriz corresponde a um
# quadrado do jogo, sendo que 0 indica um quadrado branco e -1 indica um quadrado preto. Indicar na matriz as posições que são início de
# palavras horizontais e/ou verticais nos quadrados correspondentes (substituindo os zeros), considerando que uma palavra deve ter pelo menos duas
# letras. Para isso, numere consecutivamente tais posições.



def begin(matrix1, i, j):
    return (matrix1[i][j] == 0 and
            (((j == 0 or matrix1[i][j-1] == -1) and
              (j < len(matrix1[0]) - 1 and matrix1[i][j+1] == 0)) or
             ((i == 0 or matrix1[i-1][j] == -1) and
              (i < len(matrix1) - 1 and matrix1[i+1][j] == 0))))

matrix1 = [[ 0, -1,  0, -1, -1,  0, -1,  0],
     [ 0,  0,  0,  0, -1,  0,  0,  0],
     [ 0,  0, -1, -1,  0,  0, -1,  0],
     [-1,  0,  0,  0,  0, -1,  0,  0],
     [ 0,  0, -1,  0,  0,  0, -1, -1]]

counter = 1
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        if begin(matrix1, i, j):
            matrix1[i][j] = counter
            counter += 1

print('\n'.join(('|' + ' '.join('%2i' % v for v in l) + '|') for l in matrix1))