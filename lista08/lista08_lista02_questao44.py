def calcular_produtos (vetor):
    
    principal = 1
    secundaria = 1
    
    for i in range (12):
    
        for j in range (12):
            
            if j + i < 11:
                
                secundaria *= vetor[i][j]
                
            if j > i:
                
                principal *= vetor[i][j]
    
    return principal, secundaria;

A = []

for i in range (12):
    
    A.append([0] * 12)
    
    for j in range (12):
        
        A[i][j] = int(input())

print("principal || secundaria")
print(calcular_produtos(A))
