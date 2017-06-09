def compactar (vetor):
    
    contador = 0
    compactados = 0
    
    while (contador < 100 - compactados):
        
        if vetor[contador] <= 0:
            
            vetor.remove(vetor[contador])
            compactados += 1
        
        else:
		
			contador += 1
    
    return vetor;

A = []

for i in range (100):
    
    count = int(input())
    A.append(count)
    
print(compactar(A))
