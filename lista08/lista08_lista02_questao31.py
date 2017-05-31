#----------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira             1715310001
# Frederico Victor Alfaia Rodrigues         1515200030
# Gabriel Barroso da Silva Lima             1715310011
# Nayara da Silva Cerdeira da Costa         1715310038
# Yuri Leandro de Aquino Silva              1615100462
#
#31. Faça um procedimento que receba, por parâmetro,
# duas matrizes A(4,6) e B(6,4) e retorna uma matriz C,
# também por parâmetro, que seja a diferença de M com N
#----------------------------------------------------

def diferenca_m_por_n(A, B, C):

    C = 4*[6*[None]]

    for i in range(4):
        for j in range(6):
            C[i][j] = A[i][j] - B[j][i]

    return C

A = []

for m in range(4):
    linha = []
    for n in range(6):
        linha.append(int(input('Digite o número A(%d,%d): ' %(m + 1,n + 1))))
    A.append(linha)

B = []

for m in range(6):
    linha = []
    for n in range(4):
        linha.append(int(input('Digite o número B(%d,%d): ' %(m + 1,n + 1))))
    B.append(linha)

C = []

print(diferenca_m_por_n(A,B,C))