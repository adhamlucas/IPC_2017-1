#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Gabriel de Queiroz Sousa                  1715310044
# Lucas Gabriel Silveira Duarte             1715310053
# Ian Gabriel Costa Machado                 1215120276
# Rodrigo Duarte de Souza                   1115140049
#
# Construa uma função que receba uma string como parâmetro e devolva outra string com
# os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar
# npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em
# sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.  
#----------------------------------------------------------------------------------------------------------------------
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
