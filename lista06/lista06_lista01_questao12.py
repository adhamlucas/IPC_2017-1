#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Natália Cavalcantre Xavier              1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# 12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que
# determine quantos alunos com mais de 13 anos possuem altura inferior
# à média de altura desses alunos.
# ---------------------------------------------------------------------------

idades_alunos = []
alturas_alunos = []
media_de_altura = 0
contagem_alunos = 0
qtd = 30

c = 0
while n < qtd:
    idade = int(input())
    altura = int(input())
    idades_alunos.append(idade)
    alturas_alunos.append(altura)
    media_de_altura += altura
    c += 1

media_de_altura = media_de_altura / qtd

for altura, idade in zip(alturas_alunos, idades_alunos):
    if idade > 13 and altura < media_de_altura:
       contagem_alunos += 1

print(contagem_alunos)
