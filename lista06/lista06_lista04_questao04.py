
# ---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Natália Cavalcantre Xavier              1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# Lista 4. Q 4 - Nome na vertical em escada. Modifique o programa anterior
#           de forma a mostrar o nome em formato de escada.
# -------------------------------------------------------------------------------------------------------------

nome = str(input())
print(nome[0])
for i in range(1, len(nome) + 1):
    print(nome[0:i])