#---------------------------------------------------------------------------
# Introdu��o a Programa��o de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Nat�lia Cavalcante Xavier              1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# Deseja-se publicar o n�mero de acertos de cada aluno em uma prova em forma de testes. 
# A prova consta de 30 quest�es, cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso s�o dados:

# o cart�o gabarito;
# o n�mero de alunos da turma;
# o cart�o de respostas para cada aluno, contendo o seu n�mero e suas respostas. 
#---------------------------------------------------------------------------

i = 0
gabarito = []
acertos = 0

while i < 30:
    
    print("digite o gabarito da", i+1, "� quest�o")
    resposta = input()
    gabarito.append(resposta)
    
    i += 1
    
i = 0

while i < 30:

    print("resposta da quest�o", i+1)
    resposta = input()
    
    if resposta == gabarito[i]:
    
        acertos += 1
        
    i += 1
    
print("quantidade de acertos:", acertos)
