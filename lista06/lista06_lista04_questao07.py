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
#---------------------------------------------------------------------------

#7)Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#quantos espaços em branco existem na frase.
#quantas vezes aparecem as vogais a, e, i, o, u.

frase = input("escreva a frase: ")
c = 0
quantidade = 0
quantidade_espaco = 0
while c < len(frase):
    if frase[c] == 'a' or frase[c] == 'e' or frase[c] == 'i' or frase[c] == 'o' or frase[c] == 'u':
        quantidade = quantidade + 1
    if frase[c] == ' ':
        quantidade_espaco = quantidade_espaco + 1
    c = c + 1
print("quantidade de vogais: ", quantidade)
print("quantidade de espaços: ",quantidade_espaco)
