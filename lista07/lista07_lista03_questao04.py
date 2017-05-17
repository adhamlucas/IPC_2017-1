#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Antonio Diego Furtado da Silva            1715310004
# Fangyao                                   1115180236
# Matheus de Oliveira Marques               1515310514
# Reinaldo da Silva Varas                   1715310054
# Silas Castro de Mendonça                  1715310066
#
# (Lista3_Questão 4) Escreva um programa python capaz de jogar o jogo da velha e que nunca perca.
#
#----------------------------------------------------------------------------------------------------------------------



velha = """               Posições
   |   |      0 | 1 | 2
---+---+---  ---+---+---
   |   |      3 | 4 | 5
---+---+---  ---+---+---
   |   |      6 | 7 | 8
"""
print(velha)

matriz = ['', '', '',
          '', '', '',
          '', '', '']

print("Jogador 1 = X e Jogador 2 = O")

sair = "N"
repetir = 2
velha = 0

nome1 = str(input("Digite o nome do primeiro jogador: "))
nome2 = str(input("Digite o nome do segundo jogador: "))

while sair == "N":
    for i in range(100):
        if repetir % 2 == 0:

            linha = int(input(nome1 + ", faça sua jogada: "))
            if matriz[linha] == '':
                matriz[linha] = 'X'
            else:
                print("Jogada inválida, tente novamente !")
                linha = int(input(nome1 + ", faça sua jogada: "))
                matriz[linha] = 'X'

            print('\t %s | %s | %s ' % (matriz[0], matriz[1], matriz[2]))
            print('\t---------')
            print('\t %s | %s | %s ' % (matriz[3], matriz[4], matriz[5]))
            print('\t----------')
            print('\t %s | %s | %s ' % (matriz[6], matriz[7], matriz[8]))

        else:
            linha = int(input(nome2 + ", faça sua jogada: "))
            if matriz[linha] == '':
                matriz[linha] = 'O'
            else:
                print("Jogada inválida, tente novamente !")
                linha = int(input(nome2 + ", faça sua jogada: "))
                matriz[linha] = 'O'

            print('\t %s | %s | %s ' % (matriz[0], matriz[1], matriz[2]))
            print('\t---------')
            print('\t %s | %s | %s ' % (matriz[3], matriz[4], matriz[5]))
            print('\t----------')
            print('\t %s | %s | %s ' % (matriz[6], matriz[7], matriz[8]))

        repetir += 1

        if ((matriz[0] == matriz[1] == matriz[2] == 'X'),
            (matriz[3] == matriz[4] == matriz[5] == 'X'),
            (matriz[6] == matriz[7] == matriz[8] == 'X')):
            print(nome1 + " foi o ganhador !!")
            break
        else:
            velha += 1

        if ((matriz[0] == matriz[1] == matriz[2] == 'O'),
            (matriz[3] == matriz[4] == matriz[5] == 'O'),
            (matriz[6] == matriz[7] == matriz[8] == 'O')):
            print(nome2 + " foi o ganhador !!")
            break
        else:
            velha += 1

op = input('Deseja jogar novamente ? "S"-sim ou "N"-não : ')
if op == 'N':
    matriz = ['', '', '',
              '', '', '',
              '', '', '']
