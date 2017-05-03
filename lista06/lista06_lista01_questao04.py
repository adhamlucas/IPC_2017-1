#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
vetor = input().split()
consoantes = 0
for i in vetor:
    for letra in i:
        if letra not in ["a","e","i","o","u"]:
            consoantes +=1

print(consoantes)

