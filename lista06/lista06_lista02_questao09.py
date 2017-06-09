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
#9) Escreva um algoritmo em PORTUGOL que armazene em um vetor o quadrado dos
#números ímpares no intervalo fechado de 1 a 20. Após isso, o algoritmo deve imprimir
#todos os valores armazenados.
#-----------------------------------------------------------------------------------------------------------------------

c = 1
vetor = []
while c < 20:
    if c % 2 != 0:
        vetor.append(c)
    c += 1
print(vetor)
quadrado = []
for x in vetor:
    o = x**2
    quadrado.append(o)
print(quadrado)
