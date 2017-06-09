#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Nayara da Silva Cerdeira da Costa     1715310038
# Joelson Pereira Lima 			        1715310060
# Ian Gabriel Costa Machado             1215120276
#
#20) Construa um algoritmo em PORTUGOL para calcular a média de valores PARES e
#ÍMPARES, de 50 números que serão digitados pelo usuário. Ao final o algoritmo deve
#mostrar estas duas médias. O algoritmo deve mostrar também o maior número PAR
#digitado e o menor número ÍMPAR digitado. Esses dados devem ser armazenados em
#um vetor. Além disso, devem ser impressos os valores PARES maiores que a média
#PAR, bem como os valores ÍMPARES menor que a média ÍMPAR.
#-----------------------------------------------------------------------------------------------------------------------

par = []
impa = []
for i in range(50):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        par.append(numero)
    if numero % 2 != 0:
        impa.append(numero)
c = 0
soma_par = 0
while c < len(par):
    soma_par += int(par[c])
    c += 1
i = 0
soma_impa = 0
while i < len(impa):
    soma_impa += int(impa[i])
    i += 1
size1 = int(len(par))
media_par = soma_par/size1
size2 = int(len(impa))
media_impa = soma_impa/size2
print("Media pares: ",media_par)
print("Media impa: ",media_impa)

maior = 0
for y in par:
    if y > maior:
        maior = y
menor = 3
for x in impa:
    if x < menor:
        menor = x
print("Maior par: ", maior)
print("Menor impa: ",menor)
soma = 0

for var in par:
    if var > media_par:
        soma += 1
soma2 = 0
for ver in impa:
    if ver > media_impa:
        soma2 += 1
print("impares maior que a media ",soma2)
print("pares maiores q a media ",soma)
