#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Diogo Duarte  1715310056
# Dayana Picanço 1715310058
# Walter Nobre 1715310057
matriz = []

for i in range(5):
    linha = []
    linha.append(raw_input("Nome da funcionária: "))
    linha.append(int(input("quantas 'mãos' ela fêz: "))*10)
    linha.append(int(input("quantos pés: "))*15)
    linha.append(int(input("quantos serviços de podologia: "))*30)
    matriz.append(linha)
for i in range(5):
    print("salario da %s: ") % matriz[i][0]
    print(matriz[i][1]+matriz[i][2]+matriz[i][3])
