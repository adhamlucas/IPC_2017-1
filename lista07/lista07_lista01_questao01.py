#----------------------------------------------------------------------------------------------------------------------

# 
# Aracille de Souza Barbosa                     1315120206
# Kethelen Tamara Braga Barbosa                 1525212002
# Marcus Vinicius Paes da Silva Santos          1515070060
# Ulisses Antonio Antonino da Costa             1515090555
# Uriel Brito Barros                            1515120558 
#
# 1) Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva os
# elementos da diagonal principal.
#-----------------------------------------------------------------------------------------------------------------------

matriz=[]
a=0
n_linhas = 10
n_colunas = 10
for i in range(n_linhas):
    linha = []
    for j in range(n_colunas):
        a=j+3 +a
        linha.append(a)
    matriz.append(linha)
    print(linha)

f=len(linha)
g=len(matriz)
for c in range(g):
    for d in range(f):
        if c==d:
            print(matriz[c][d], end=" ")
