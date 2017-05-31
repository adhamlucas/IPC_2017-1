#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

n=[1,2,7]
def funcao(n):
    valor = n[::-1]
    return valor
resultado= funcao(n)
for i in range(len(resultado)):
    print(resultado[i], end=" ")

