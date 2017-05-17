#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Joelson Pereira Lima 			        1715310060
# Víctor Hugo de Oliveira Carreira      1715310063
#18)
#A  matriz  dados  contém  na  1ª  coluna  a  matrícula  do  aluno
#no  curso
#;  na  2ª,  o  sexo  (0
#para feminino e 1 para masculino); na 3ª, o código do curso, e na 4ª, o CR (Coeficiente
#de Rendimento).
#Suponha 10 alunos e que o CR é um número inteiro.
#Faça um algor
#itmo que armazene esses dados sabendo
#-
#se que:
#-
#O  código  do  curso  é  uma  parte  d
#e  um  número  de
#matrícula:  aasccccnnn  (aa  ano,  s
#semestre,  ccc  código  do  curso  e  nnn  matrícula  no  curso)
#,  que  deve  ser  lido;  Além,
#disso, o sexo e o CR devem ser lidos também.
#Um  g
#rupo  empresarial  resolveu  premiar  a  aluna  com  CR  mais  alto  de  um  curso  cujo
#código deverá ser digitado
#
#-----------------------------------------------------------------------------------------------------------------------

colunas = 4
linhas = 2
matriz = []
curso = []
maior = 0
c = 0
for i in range(linhas):
    linha = []
    for j in range(colunas):
       linha.append(input())
    matriz.append(linha)

codigo_do_curso = input("curso:")

for i in range (linhas):
    if matriz[i][2] == codigo_do_curso:
        curso.append(matriz[i])

size = len(curso)

while c < (size-1):
    for x in range(size):
        if curso[x][3] > curso[c][3]:
            maior += 1
        if maior == (size-1):
            print(curso[x],"ganhou")
    c += 1




