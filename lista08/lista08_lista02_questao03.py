#---------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Jandinne Duarte de Oliveira                   1015070265
# Wesley da Silva Rocha                         1715310026 
#
# Foi realizada uma pesquisa entre 500 habitantes de uma certa região.
# De cada habitante foram coletados os dados: idade, sexo, salário e
# número de filhos. Faça um procedimento que leia esses dados em um
# vetor de registro. O vetor de registro deve ser enviado por
# referência.
# 
#---------------------------------------------------------------------

def armazena_dados(dados):
    for i in range(len(dados)):
        dado = input().split()
        dados[i] = {\
            "idade": dado[0],\
            "sexo": dado[1],\
            "salário": dado[2],\
            "número de filhos": dado[3]}

n = int(input())
dados = n*[None]
armazena_dados(dados)
for dado in dados:
    print(dado)

