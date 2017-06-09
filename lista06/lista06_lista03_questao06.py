#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Dayana Picanço Marquez            1715310058
# Vitor Simões Azevedo              1715310025
# Wilbert Luís Evangelista Marins   1715310055
# Enrique Leão Barbosa Izel         1715310048
# Edson de Lima Barros              1715310043
# Víctor Hugo de Oliveira Carreira  1715310063
#
#6)Dados dois strings (um contendo uma frase e outro contendo uma palavra), 
#determine o número de vezes que a palavra ocorre na frase.
#Exemplo:
#Para a palavra ANA e a frase :
#ANA E MARIANA GOSTAM DE BANANA
#Temos que a palavra ocorre 4 vezes na frase.
#---------------------------------------------------------------------------

frase = input()
palavra = input()
tam1 = len(frase)
tam2 = len(palavra)
i = 0
cont = 0
for i in range(tam1):
        c = 0
        j = i
        k = 0
        while j < tam2 + i and j < tam1:
                if palavra[k] == frase[j]:
                        c+=1
                k += 1
                j += 1
        if c == tam2:
                cont += 1
print('Temos que a palavra ocorre' ,cont ,'vezes na frase.')
