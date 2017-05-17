# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Gabriel barroso da Silva Lima                      1715310011
# Frederico Victor Alfaia Rodrigues                  1515200030
# André Neves
# Diego Figueira
# Diogo Duarte
#
# Criar um algoritmo que leia uma matriz ANxN (N <= 10) e verifique (informe) se tal
# matriz é ou não simétrica (At = A).

matriz = []
N = int(input())

for i in range (N):
    
    matriz.append([0]*N)
    
    for j in range (N):
        
        matriz[i][j] = int(input())
        
i = 0

while i < N:
    
    j = 0
    
    while j < N:
        
        if matriz[i][j] != matriz[j][i]:
        
            i = N
            j = N
        
        else:
            
            j += 1
        
    i += 1
    
if i == N:
    
    print("Matriz simétrica")
    
else:
    
    print("Matriz não simétrica")
