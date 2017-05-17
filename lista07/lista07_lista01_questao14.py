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
# 14) Ler  uma  matriz  4x5  de  inteiros,  calcular  e  imprimir  a  soma  de  todos  os  seus elementos.
#-----------------------------------------------------------------------------------------------------------------------

matriz = []
soma = 0                # soma de todos os itens da matriz
m = 4                   # linha
n = 5                   # coluna

for i in range(m):
    coluna = []
    for j in range(n):
        valor=int(input("valor: "))     #caso necessite entrada de valores
        coluna.append(valor)            # ou    valor
    matriz.append(coluna)

for d in range(len(matriz)):
    for c in range(len(coluna)):
        soma = matriz[d][c] + soma

print(matriz)
print("Soma total : ", soma)
