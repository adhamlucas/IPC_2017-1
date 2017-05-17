#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Aracille de Souza Barbosa                     1315120206
# Kethelen Tamara Braga Barbosa                 1525212002
# Marcus Vinicius Paes da Silva Santos          1515070060
# Ulisses Antonio Antonino da Costa             1515090555
# Uriel Brito Barros                            1515120558 
# 
# 22) Criar um algoritmo que entre com valores inteiros para uma matriz m 3 x 3
# e imprima a matriz final, conforme mostrado a seguir:
#------------------------------------------------------------------------------

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor=int(input("valor: "))
        linha.append(valor)
    matriz.append(linha)
    linha.reverse()
matriz.reverse()
print(matriz)
