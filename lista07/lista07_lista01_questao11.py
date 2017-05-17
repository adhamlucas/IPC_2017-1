# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Gabriel barroso da Silva Lima      1715310011
# Frederico Victor Alfaia Rodrigues  1515200030
# André Luis Laborda neves           1515070006
# Diego Reis Figueira                1515070169
# Diogo Duarte
#
# Entrar com valores para uma matriz A3x4. Gerar e imprimir uma matriz B que é o
# triplo da matriz A.


matriz = []
triplo = []

for i in range (3):
    
    matriz.append([0]*3)
    
    for j in range (4):
        
        matriz[i][j] = int(input())
        
for i in range (3):
    
    triplo.append([0]*3)
    
    for j in range (4):
        
        triplo[i][j] = matriz[i][j] * 3
