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
# Lista 4. Q 1 - Tamanho de strings. Faça um programa que leia 2 strings
#  e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento
#  e são iguais ou diferentes no conteúdo.

# -------------------------------------------------------------------------------------------------------------

string1 = str(input())
string2 = str(input())

print("Compara duas strings")

print("String 1: %s" % string1)
print("String 2: %s" % string2)

print("Tamanho de: %s, %d" % (string1, len(string1)))
print("Tamanho de: %s, %d" % (string2, len(string2)))

if len(string1) != len(string2):
    print("As duas strings são de tamanhos diferentes.")
else:
    print("As duas strings são de tamanhos iguais.")

if string1 == string2:
    print("As duas strings possuem conteúdo iguais.")
else:
    print("As duas strings possuem conteúdo diferente.")