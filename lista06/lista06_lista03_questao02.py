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

# o cartão gabarito;
# o número de alunos da turma;
# o cartão de respostas para cada aluno, contendo o seu número e suas respostas. 
#---------------------------------------------------------------------------

i = 0
gabarito = []
acertos = 0

while i < 30:
    
    print("digite o gabarito da", i+1, "ª questão")
    resposta = input()
    gabarito.append(resposta)
    
    i += 1
    
i = 0

while i < 30:

    print("resposta da questão", i+1)
    resposta = input()
    
    if resposta == gabarito[i]:
    
        acertos += 1
        
    i += 1
    
print("quantidade de acertos:", acertos)
