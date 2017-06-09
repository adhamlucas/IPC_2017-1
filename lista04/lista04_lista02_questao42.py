#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
# Erik Atlio Silva Rey                  1715310059
# Edson de Lima Barros                  1715310043
# Enrique Leão Barbosa Izel             1715310048
# Evandro Padilha Barroso Filho         1715310009
# Fang Yao                              1115180236
#
#42.Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em
#branco e em seguida, os valores na sequência como foram lidos.
#Entrada:
#   A entrada contem três números inteiros.
#Saída:
#   Imprima a saída conforme foi especificado.
#-----------------------------------------------------------------------------------------------------------------------

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

lower = a
if b < lower:
    lower = b
if c < lower:
    lower = c

higher = a
if b > higher:
    higher = b
if c > higher:
    higher = c

mid = a + b + c - higher - lower

print(lower)
print(mid)
print(higher)
print()
print(a)
print(b)
print(c)
