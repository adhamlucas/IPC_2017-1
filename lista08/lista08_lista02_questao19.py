# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Aracille de Souza Barbosa              1315120206
# Diego Reis Figueira                    1515070169
# Kethelen Tamara Braga Barbosa          1525212002
# Marcus Vinicius Paes da Silva Santos   1515070060
# Ulisses Antonio Antonino da Costa      1515090555
#
# 19. Faça um procedimento que recebe, por parâmetro, 2 vetores de 15 elementos inteiros
# e que calcule e retorne, também por parâmetro, o vetor produto dos dois primeiros
# ----------------------------------------------------------

# função que retorna o produto de dois vetores de inteiros

def vetor_produto(v1, v2):
    vetor_produto = []


    for i in range(0, 15):

        vetor_produto.append(v1[i]*v2[i])
    return vetor_produto


limit = 15
count = 0
vetor1 = []

while count < limit:
    number = int(input("Digite um valor "))
    vetor1.append(number)
    count += 1

count = 0
vetor2 = []

while count < limit:
    number = int(input("Digite um valor "))
    vetor2.append(number)
    count += 1


vetorproduto = vetor_produto(vetor1, vetor2)
print(vetorproduto)