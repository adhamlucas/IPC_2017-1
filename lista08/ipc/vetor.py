# Biblioteca de funções para os vetores

import random


# lista 1 questão 1
def exercicio_1(n):
    for i in range(n):
        i += 1
        print ((str(i) + " " )* i)
    return  i


# lista 1 questao 2

def SequencialAbaixoDiagonalPrincipal(n):
    res = ""
    for i in range(n):
        for j in range(i + 1):
            res += (str(j + 1) + " ")
        res += "\n"
    return res

# lista 1 questão 10
# função que recebe 3 argumentos e retorna a soma deles
def somar_tres(a,b,c):
    return (a+b+c)

# lista 1 questao 10
# função que sorteia valores com dois dados
def jogar_dados():
    dados = [random.randint(1, 6), random.randint(1, 6)]
    dados = dados[0] + dados[1]
    return dados


# função para retornar uma lista a partir de uma entrada em sequência
# Ex.: Em um input: 4 10 PM, retornará a lista: ['4', '10', 'PM']

def get_as_uri(valores):
    valores = valores.split()

    return valores


# função para retornar uma lista de inteiros a partir de uma entrada em sequência
# Ex.: Em um input: 4 5 6 3 2, retornará a lista: [4, 5, 6, 3, 2]

def get_as_uri_inteiros(valores):
    valores = valores.split()
    valores_int = []

    for i in valores:
        valores_int.append(int(i))

    return valores_int


# usada na lista 2 questão 22
# função para criar vetor de tamanho n
def cria_vetor(n):
    vetor = []
    for j in range(n):
        # serão inseridos valores aleatórios na matriz (entre 1 e 4)
        value = random.randint(1, 4)
        vetor.append(value)
    return vetor


# função que gera números decimais aleatórios entre n e n
def gera_aleatorio_float(n, m):
    res = float('%2.1f' % (random.random() * random.randint(n, m)))
    return res


# função para criar vetor de tamanho n
def cria_vetor_numeros_decimais(n):
    vetor = []
    for j in range(n):
        # serão inseridos valores aleatórios na matriz (entre 1 e 4)
        value = gera_aleatorio_float(1, 4)
        vetor.append(value)
    return vetor


# função que retorna  o maior elemento em um vetor
def maior_valor_do_vetor(vetor):
    maior = vetor[0]
    for i in vetor:
        if i > maior:
            maior = i
    return maior


# função que  retorna o menor elemento em um vetor
def menor_valor_do_vetor(vetor):
    menor = vetor[0]
    for i in vetor:
        if i < menor:
            menor = i
    return menor


# função que  retorna a média dos elementos

def media_dos_valores_do_vetor(vetor):
    soma = 0
    for i in vetor:
        soma += i

    return soma / len(vetor)


# função que divide todos os elementos de um vetor por um número
def divide_todos_por_numero(vetor, numero):
    novo_vetor = []
    for i in vetor:
        novo_vetor.append("%2.3f" % (i / numero))
    return novo_vetor


# lista 2 questão 17
# função que retorna a diferença entre dois vetores de inteiros

def diferenca(vetor1, vetor2):

    vetor_diferenca = []
    tam = len(vetor1)

    for i in range(tam):
        if vetor2.count(vetor1[i]) == 0:
            if vetor_diferenca.count(vetor1[i]) == 0:
                vetor_diferenca.append(vetor1[i])

    return vetor_diferenca


# lista 2 questão 16
# função que retorna a intersecção entre dois vetores de inteiros

def vetor_interseccao(vetor1, vetor2):
    return list(set(vetor1) & set(vetor2))


# lista 2 questão 18
# função que retorna a soma de dois vetores de inteiros

def vetor_soma(vetor1, vetor2):
    vetor = []

    for i, j in zip(vetor1, vetor2):
        vetor.append(i + j)

    return vetor

# lista 2 questão 19
# função que retorna o produto de dois vetores de inteiros

def vetor_produto(vetor1, vetor2):
    vetor = []

    for i, j in zip(vetor1, vetor2):
        vetor.append(i * j)

    return vetor

# lista02_questao20
# Faça um procedimento que receba, por parâmetro,
#  um vetor K(15)
def criar_vetor_tamanho15():
    vetor = []
    
    for x in range(15):
        vetor.append(float(input('Digite o %dº valor: ' % (x + 1))))
    
    return vetor
#lista02_questao20
#retorna um vetor P com os números primos do vetor pasado como argumento
def criar_vetor_primo(vetor):
    P = []
    
    for x in(vetor):
        divisores = 0
        for i in range(1, int(x) + 1):
            if x % i == 0:
                divisores += 1
        if divisores == 2:
            P.append(x)
    
    return P

#lista02_questao21
#receber um vetor e compactá-lo, eliminando números nulos e negativos
def compactar (vetor):
    
    contador = 0
    compactados = 0
    
    while (contador < 100 - compactados):
        
        if vetor[contador] <= 0:
            
            vetor.remove(vetor[contador])
            compactados += 1
        
        else:
		
			contador += 1
    
    return vetor;

#lista02_questao44
#receber um vetor e calcular o produto dos elementos acima da diagonal secundaria e principal
def calcular_produtos (vetor):
    
    principal = 1
    secundaria = 1
    
    for i in range (12):
    
        for j in range (12):
            
            if j + i < 11:
                
                secundaria *= vetor[i][j]
                
            if j > i:
                
                principal *= vetor[i][j]
    
    return principal, secundaria;
