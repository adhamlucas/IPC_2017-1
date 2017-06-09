#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Natália Cavalcante Xavier              1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. 
# A prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso são dados:

# Dadas duas seqüências com n números inteiros entre 
# 0 e 9, interpretadas como dois números inteiros
# de n algarismos, calcular a seqüência de números que 
# representa a soma dos dois inteiros.
#---------------------------------------------------------------------------

n = int(input("número de algarismo de cada termo: "))
i = 0
primeiro = []
segundo = []
resultado = []
sobra = 0

print("defina o primeiro termo:")

while i < n:

    termo = int(input())
    
    while 0 > termo > 10:
        
        termo = int(input("algarismo inválido, digite outro: "))
        
    primeiro.append(termo)
    i += 1
    
i = 0    

print("defina o segundo termo:")

while i < n:

    termo = int(input())
    
    while 0 > termo > 10:
        
        termo = int(input("algarismo inválido, digite outro: "))
        
    segundo.append(termo)
    i += 1

i = 0

while i < n:

    if (primeiro[i] + segundo[i]) >= 10:
        
        resultado.append(((primeiro[i] + segundo[i]) - 10) + sobra)
        sobra = 1
        
    else:
        
        resultado.append((primeiro[i] + segundo[i]) + sobra)
        sobra = 0
        
    i += 1
    
if sobra == 1:
    
    resultado.append(1)
    n += 1
    
i = 0
resultado.reverse()

while i < n:
    
    print(resultado[i])
    i += 1
