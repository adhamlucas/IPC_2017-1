#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Dayana Picanço Marquez            1715310058
# Vitor Simões Azevedo              1715310025
# Wilbert Luís Evangelista Marins   1715310055
# Enrique Leão Barbosa Izel         1715310048
# Edson de Lima Barros              1715310043
# Víctor Hugo de Oliveira Carreira  1715310063
# Lista 3 - Questão 17 Dada uma seqüência de n números inteiros, determinar um segmento de soma máxima.
# Exemplo: Na seqüência 5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1 , a soma do segmento é 33.
#-------------------------------------------------------------------------------------------------------------
cont = 0
sum = 0
n = int(input("Digite o tamanho da sequencia"))
lista = []

while cont < n:
    number = int(input("Digite um numero inteiro"))
    lista.append(number)
    cont = cont +1
print(lista)

for element in lista:
    if element > 0:
        sum = sum + element
print("A soma do segmento é",sum)


