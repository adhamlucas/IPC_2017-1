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
#13) Escreva um algoritmo em PORTUGOL que receba dez números do usuário e
#armazene em um vetor o cubo de cada número. Após isso, o algoritmo deve imprimir
#todos os valores armazenados.
#-----------------------------------------------------------------------------------------------------------------------


lista = []
for i in range(0, 10):
    numero = int(input("aaaa"))

    lista.append(numero**3)
print(lista)
