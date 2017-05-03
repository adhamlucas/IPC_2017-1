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
# Lista 4. Q 5 - Nome na vertical em escada invertida.
# Altere o programa anterior de modo que a escada seja invertida.

# -------------------------------------------------------------------------------------------------------------

nome = str(input())

for i in range(len(nome) + 1,1,-1):
    print(nome[0:i])
print(nome[0])
