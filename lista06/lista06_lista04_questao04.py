
# ---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Lista 4. Q 4 - Nome na vertical em escada. Modifique o programa anterior
#           de forma a mostrar o nome em formato de escada.
# -------------------------------------------------------------------------------------------------------------

nome = str(input())
print(nome[0])
for i in range(1, len(nome) + 1):
    print(nome[0:i])