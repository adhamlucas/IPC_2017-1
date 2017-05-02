# ---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Dayana Picanço Marquez            1715310058
# Vitor Simões Azevedo              1715310025
# Wilbert Luís Evangelista Marins   1715310055
# Enrique Leão Barbosa Izel         1715310048
# Edson de Lima Barros              1715310043
# Víctor Hugo de Oliveira Carreira  1715310063

# 28) Fazer um algoritmo em PORTUGOL que:
# a) Leia uma variável composta A com 30 valores numéricos distintos;
# b) Leia outra variável composta B com 30 valores numéricos;
# c) Leia o valor de uma variável X;
# d) Verifique qual o elemento de A que é igual a X;
# e) Imprima o elemento de B de posição correspondente à do elemento de A igual a X..
# ---------------------------------------------------------------------------
list_a = list(range(1, 30))
list_b = 30 * [6]
x = int(input())
print(list_a.index(x))
print(list_b[list_a.index(x)])
