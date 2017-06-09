# ---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Luiz Paulo Machado e Souza          1515200542
# FANG YAO                            1115180236
# FELIPE GUERREIRO DE MELLO           1315120052
# YURI LEANDRO DE AQUINO SILVA        1615100462

# Escreva um algoritmo em PORTUGOL que receba quinze números do usuário e
#armazene em um vetor a raiz quadrada de cada número. Caso o valor digitado seja
#menor que zero o número –1 deve ser atribuído ao elemento do vetor. Após isso, o
#algoritmo deve imprimir todos os valores armazenados.

# ---------------------------------------------------------------------------
vet = []
raiz = []
a = -1
for i in range (0,14):
    n = int(input())
    vet.append(n)

for i in range(len(vet)):
    if vet[i]<0:
        x = vet[i]**0.5
        raiz.append(x)
    else:
        raiz.append(-1)

print(raiz)
