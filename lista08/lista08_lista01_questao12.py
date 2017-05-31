import random

def embaralhar_palavra(word):
    word = word.lower()
    posicion = []

    word2 = ''

    while len(word) != len(posicion):

        vari = random.randint(0,len(word)-1)

        if vari not in posicion:
            posicion.append(vari)
            word2 += word[vari]

    return word2


word = input('Digite uma palavra: ')

print(embaralhar_palavra(word))
