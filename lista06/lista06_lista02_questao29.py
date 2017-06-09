#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Nayara da Silva Cerdeira da Costa     1715310038
# Joelson Pereira Lima 			        1715310060
# Ian Gabriel Costa Machado             1215120276
#
#29) Fazer um algoritmo em PORTUGOL que:
#a) Leia o valor inteiro de M (M  30) e os M valores de uma variável composta A;
#b) Leia o valor inteiro de N (N  20) e os N valores de um variável composta B;
#c) Determine o conjunto C = A  B (união de A com B), onde C não deverá conter
#elementos repetidos (A e B não contêm elementos repetidos);
#d) Imprima os elementos contidos em A, B e C
#-----------------------------------------------------------------------------------------------------------------------

listaA = []
a = input("Digite valores inteiros <= 30: ").split()
for c in a:
    if int(c) <= 30:
        listaA.append(c)
listaB = []
b = input("Digite valores inteiros <= 20: ").split()
for i in b:
    if int(i) <= 20:
        listaB.append(i)
listaC = []
size1 = int(len(listaA))
x = 0
while x < size1:
    m = int(listaA[x])
    n = int(listaB[x])
    if m != n:
        listaC.append(m)
        listaC.append(n)
    x += 1
listaC.sort()
print(listaA)
print(listaB)
print(listaC)
