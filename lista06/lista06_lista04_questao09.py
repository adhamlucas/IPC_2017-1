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
# Lista 4. Q 9 - Verificação de CPF. Desenvolva um programa que
# solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
# e indique se é um número válido ou inválido através da validação dos
# dígitos verificadores e dos caracteres de formatação.

# -------------------------------------------------------------------------------------------------------------

nome = str(input())

for i in range(len(nome) + 1,1,-1):
    print(nome[0:i])
print(nome[0])
