#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Aracille de Souza Barbosa                     1315120206
# Kethelen Tamara Braga Barbosa                 1525212002
# Marcus Vinicius Paes da Silva Santos          1515070060
# Ulisses Antonio Antonino da Costa             1515090555
# Uriel Brito Barros                            1515120558 
#
# 3) Dadas duas matrizes reais  Amxn e Bnxp, calcular o produto de A por B. 
#-----------------------------------------------------------------------------------------------------------------------

matriz_a=[]
matriz_b=[]
m=5      #linha matriz_a
n=5      #coluna matriz_a
o=5      #linha matriz_b
p=5      #coluna matriz_a
valor_a=0
valor_b=0
for i in range(m):
    coluna_a = []
    for j in range(n):
        valor_a=int(input("digite valor: "))
        coluna_a.append(valor_a)  
    matriz_a.append(coluna_a)
#print(matriz_a)       
for a in range(o):
    coluna_b = []
    for b in range(p):
        valor_b=int(input("digite valor: "))
        coluna_b.append(valor_b) 
    matriz_b.append(coluna_b)
#print(matriz_b)

if o == n:
    sizeLA = len(matriz_a)
    sizeCA = len(matriz_a[0])  # deve ser igual a sizeLB para ser possível multiplicar as matrizes
    sizeCB = len(matriz_b[0])
    matrizR = []
    # Multiplica
    for i in range(sizeLA):
        matrizR.append([])
        for j in range(sizeCB):
            val = 0
            for k in range(sizeCA):
                val += matriz_a[i][k] * matriz_b[k][j]
            matrizR[i].append(val)
print(matrizR)
