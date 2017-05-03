# ---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Lista 4. Q 5 - Nome na vertical em escada invertida.
# Altere o programa anterior de modo que a escada seja invertida.

# -------------------------------------------------------------------------------------------------------------

nome = str(input())

for i in range(len(nome) + 1,1,-1):
    print(nome[0:i])
print(nome[0])