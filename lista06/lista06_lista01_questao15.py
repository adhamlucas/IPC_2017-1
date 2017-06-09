#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Antônio Diego Furtado da Silva         1715310004
# Aracille de Souza Barbosa              1315120206
# Marcus Vinicius Paes da Silva Santos   1515070060
# Silas Castro de Mendonça               1715310066
# Wesley da Silva Rocha                  1715310026
#
#15) Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de
#dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;
#-----------------------------------------------------------------------------------------------------------------------

valores = input().split()
size = int(len(valores))
numeros = []
soma = 0
c = 0

while c < size:
    var = valores[c]
    if var != "-1":
        numeros.append(var)
        soma += int(var)
    c += 1
print("a quantidade de valores que foram lidos =", size - 1)
print("os valores na ordem em que foram informados, um ao lado do outro:")
for x in numeros:
    print(x, end=" ")
print(" ")
numeros.reverse()
print("os valores na ordem inversa à que foram informados, um abaixo do outro:")
for i in numeros:
    print(i)

print("a soma dos valores =", soma)
media = soma/(size - 1)
print("a média dos valores=", media)

count = 0
acima = 0
abaixo = 0
while count < len(numeros):
    verificar = int(numeros[count])
    if verificar > float(media):
        acima += 1
    if verificar < 7:
        abaixo += 1
    count += 1
print("a quantidade de valores acima da média calculada:", acima)
print("a quantidade de valores abaixo de sete:", abaixo)
print("HUEHEUHEUHEUHEU.....FIM")
