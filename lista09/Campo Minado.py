import os
import random

def mover_para_cima(tabuleiro, descobertos, posicao_numero, posicao_letra, valores):

    descobertos[posicao_numero][posicao_letra] = 1

    if tabuleiro[posicao_numero][posicao_letra] == 0:

        if posicao_numero != 0:

            if descobertos[posicao_numero - 1][posicao_letra] == 0:

                descobertos, valores = mover_para_cima(tabuleiro, descobertos, posicao_numero - 1, posicao_letra, valores + 1)

        if posicao_letra != 0:

            if descobertos[posicao_numero][posicao_letra - 1] == 0:

                descobertos, valores = mover_para_esquerda(tabuleiro, descobertos, posicao_numero, posicao_letra - 1, valores + 1)

        if posicao_letra != 15:

            if descobertos[posicao_numero][posicao_letra + 1] == 0:

                descobertos, valores = mover_para_direita(tabuleiro, descobertos, posicao_numero, posicao_letra + 1, valores + 1)

    return descobertos, valores


def mover_para_baixo(tabuleiro, descobertos, posicao_numero, posicao_letra, valores):

    descobertos[posicao_numero][posicao_letra] = 1

    if tabuleiro[posicao_numero][posicao_letra] == 0:

        if posicao_numero != 15:

            if descobertos[posicao_numero + 1][posicao_letra] == 0:

                descobertos, valores = mover_para_baixo(tabuleiro, descobertos, posicao_numero + 1, posicao_letra, valores + 1)

        if posicao_letra != 0:

            if descobertos[posicao_numero][posicao_letra - 1] == 0:

                descobertos, valores = mover_para_esquerda(tabuleiro, descobertos, posicao_numero, posicao_letra - 1, valores + 1)

        if posicao_letra != 15:

            if descobertos[posicao_numero][posicao_letra + 1] == 0:

                descobertos, valores = mover_para_direita(tabuleiro, descobertos, posicao_numero, posicao_letra + 1, valores + 1)

    return descobertos, valores


def mover_para_esquerda(tabuleiro, descobertos, posicao_numero, posicao_letra, valores):

    descobertos[posicao_numero][posicao_letra] = 1

    if tabuleiro[posicao_numero][posicao_letra] == 0:

        if posicao_letra != 0:

            if descobertos[posicao_numero][posicao_letra - 1] == 0:

                descobertos, valores = mover_para_esquerda(tabuleiro, descobertos, posicao_numero, posicao_letra - 1, valores + 1)

        if posicao_numero != 0:

            if descobertos[posicao_numero - 1][posicao_letra] == 0:

                descobertos, valores = mover_para_cima(tabuleiro, descobertos, posicao_numero - 1, posicao_letra, valores + 1)

        if posicao_numero != 15:

            if descobertos[posicao_numero + 1][posicao_letra] == 0:

                descobertos, valores = mover_para_baixo(tabuleiro, descobertos, posicao_numero + 1, posicao_letra, valores + 1)

    return descobertos, valores


def mover_para_direita(tabuleiro, descobertos, posicao_numero, posicao_letra, valores):

    descobertos[posicao_numero][posicao_letra] = 1

    if tabuleiro[posicao_numero][posicao_letra] == 0:

        if posicao_letra != 15:

            if descobertos[posicao_numero][posicao_letra + 1] == 0:

                descobertos, valores = mover_para_direita(tabuleiro, descobertos, posicao_numero, posicao_letra + 1, valores + 1)

        if posicao_numero != 0:

            if descobertos[posicao_numero - 1][posicao_letra] == 0:

                descobertos, valores = mover_para_cima(tabuleiro, descobertos, posicao_numero - 1, posicao_letra, valores + 1)

        if posicao_numero != 15:

            if descobertos[posicao_numero + 1][posicao_letra] == 0:

                descobertos, valores = mover_para_baixo(tabuleiro, descobertos, posicao_numero + 1, posicao_letra, valores + 1)

    return descobertos, valores


def procurar_espacos(tabuleiro, descobertos, posicao_numero, posicao_letra, valores):

    descobertos[posicao_numero][posicao_letra] = 1
    valores += 1

    if posicao_numero != 0:

        if descobertos[posicao_numero - 1][posicao_letra] == 0:

            descobertos, valores = mover_para_cima(tabuleiro, descobertos, posicao_numero - 1, posicao_letra, valores + 1)

    if posicao_letra != 0:

        if descobertos[posicao_numero][posicao_letra - 1] == 0:

            descobertos, valores = mover_para_esquerda(tabuleiro, descobertos, posicao_numero, posicao_letra - 1, valores + 1)

    if posicao_numero != 15:

        if descobertos[posicao_numero + 1][posicao_letra] == 0:

            descobertos, valores = mover_para_baixo(tabuleiro, descobertos, posicao_numero + 1, posicao_letra, valores + 1)

    if posicao_letra != 15:

        if descobertos[posicao_numero][posicao_letra + 1] == 0:

            descobertos, valores = descobertos = mover_para_direita(tabuleiro, descobertos, posicao_numero, posicao_letra + 1, valores + 1)

    return descobertos, valores


def converter_letra(letra):

    if letra == "A" or letra == "a":

        return 0

    elif letra == "B" or letra == "b":

        return 1

    elif letra == "C" or letra == "c":

        return 2

    elif letra == "D" or letra == "d":

        return 3

    elif letra == "E" or letra == "e":

        return 4

    elif letra == "F" or letra == "f":

        return 5

    elif letra == "G" or letra == "g":

        return 6

    elif letra == "H" or letra == "h":

        return 7

    elif letra == "I" or letra == "i":

        return 8

    elif letra == "J" or letra == "j":

        return 9

    elif letra == "K" or letra == "k":

        return 10

    elif letra == "L" or letra == "l":

        return 11

    elif letra == "M" or letra == "m":

        return 12

    elif letra == "N" or letra == "n":

        return 13

    elif letra == "O" or letra == "o":

        return 14

    elif letra == "P" or letra == "p":

        return 15

    else:

        return -1


def montar_tabuleiro(imagem, escolhidos):

    for i in range (9):

        print("  ", i+1, end=" ")

        for j in range(16):

            if j != 15:

                if escolhidos[i][j] == 1:

                    if imagem[i][j] != -1:

                        print("|", imagem[i][j], end=" ")

                    else:

                        print("| *", end=" ")

                else:

                    print("| X", end=" ")

            else:

                if escolhidos[i][j] == 1:

                    if imagem[i][j] != -1:

                        print("|", imagem[i][j],)

                    else:

                        print("| *")

                else:

                    print("| X")

                print("  --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")

    for i in range (9, 16):

        print(" ", i + 1, end=" ")

        for j in range(16):

            if j != 15:

                if escolhidos[i][j] == 1:

                    if imagem[i][j] != -1:

                        print("|", imagem[i][j], end=" ")

                    else:

                        print("| *", end=" ")

                else:

                    print("| X", end=" ")

            else:

                if escolhidos[i][j] == 1:

                    if imagem[i][j] != -1:

                        print("|", imagem[i][j])

                    else:

                        print("| *")

                else:

                    print("| X")

                if i != 15:

                    print("  --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")


def desenhar_tabuleiro(imagem, escolhidos):

    for i in range(espacos_de_diferenca):
        print("")

    print("       A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P")
    print("         |   |   |   |   |   |   |   |   |   |   |   |   |   |   |")

    montar_tabuleiro(imagem, escolhidos)

    print("")


def jogo():

    game = 0

    while game == 0:

        jogo = 0

        for i in range(espacos_de_diferenca):
            print("")

        print("modo de jogo:")
        print("facil (20 minas) - 1 || médio (40 minas) - 2 || dificil (60 minas) - 3")
        print("")
        modo_de_jogo = int(input("Defina o modo de jogo: "))

        while modo_de_jogo < 1 or modo_de_jogo > 3:
            modo_de_jogo = int(input("Opção inválida, digite uma das opções válidas"))

        tabuleiro = []
        jogados = []
        val = [0, 0]
        descobertos = 0

        for i in range (16):

            tabuleiro.append([0] * 16)

        modo_de_jogo *= 20

        for i in range (modo_de_jogo):

            minax = random.randint(0, 15)
            minay = random.randint(0, 15)

            while tabuleiro[minax][minay] == -1:

                minax = random.randint(0, 15)
                minay = random.randint(0, 15)

            tabuleiro[minax][minay] = -1

        for i in range (16):

            jogados.append([0]*16)

        num_piso = 0
        limite_x = 0
        limite_y = 0

        print("")
        print("")
        print("")

        for i in range (16):

            for j in range (16):

                if i == 0:

                    limite_y = 1

                if j == 0:

                    limite_x = 1

                if i == 15:

                    limite_y = 2

                if j == 15:

                    limite_x = 2

                if tabuleiro[i][j] != -1:

                    if limite_y != 1:

                        if limite_x != 1:

                            if tabuleiro[i-1][j-1] == -1:

                                num_piso += 1

                        if tabuleiro[i-1][j] == -1:

                            num_piso += 1

                        if limite_x != 2:

                            if tabuleiro[i-1][j+1] == -1:

                                num_piso += 1

                    if limite_x != 1:

                        if tabuleiro[i][j-1] == -1:

                            num_piso += 1

                    if limite_x != 2:

                        if tabuleiro[i][j+1] == -1:

                            num_piso += 1

                    if limite_y != 2:

                        if limite_x != 1:

                            if tabuleiro[i+1][j-1] == -1:

                                num_piso += 1

                        if tabuleiro[i+1][j] == -1:

                            num_piso += 1

                        if limite_x != 2:

                            if tabuleiro[i+1][j+1] == -1:

                                num_piso += 1

                    tabuleiro[i][j] = num_piso

                limite_x = 0
                limite_y = 0
                num_piso = 0

        desenhar_tabuleiro(tabuleiro, jogados)

        while jogo == 0:

            confere_jogada = 0

            while confere_jogada == 0:

                print("")
                i = input("Escolha uma coluna (A-P): ")
                val[0] = converter_letra(i)

                while val[0] == -1:

                    print("")
                    i = input("Coluna inválida, escolha uma de A a P")
                    val[0] = converter_letra(i)

                i = input("Escolha uma linha (1-16): ")
                val[1] = int(i)

                while val[1] < 1 or val[1] > 16:

                    i = input("Linha inválida, escolha uma de 1 a 16")
                    val[1] = int(i)

                val[1] -= 1

                if jogados[val[1]][val[0]] == 0:

                    confere_jogada = 1

                else:

                    print("")
                    print("Casa já preenchida, faça outra jogada")

            if tabuleiro[val[1]][val[0]] == -1:

                jogo = 1

                for i in range (16):

                    for j in range (16):

                        jogados[i][j] = 1

                descobertos = 256 - modo_de_jogo

                desenhar_tabuleiro(tabuleiro, jogados)

            elif tabuleiro[val[1]][val[0]] != 0:

                jogados[val[1]][val[0]] = 1
                descobertos += 1
                desenhar_tabuleiro(tabuleiro, jogados)

            else:

                jogados, descobertos = procurar_espacos(tabuleiro, jogados, val[1], val[0], descobertos)
                descobertos = 0

                for i in range (16):

                    for j in range (16):

                        if jogados[i][j] == 1:

                            descobertos += 1

                if descobertos == 256 - modo_de_jogo:

                    for i in range(16):

                        for j in range(16):

                            jogados[i][j] = 1

                desenhar_tabuleiro(tabuleiro, jogados)

            if descobertos + modo_de_jogo == 256 and jogo == 0:

                jogo = 2

        if jogo == 1:

            print("Que pena, você perdeu!")

        else:

            print("Você ganhou!!!")

        print("")
        print("Jogar novamente - 0 || Ir para menu - 1")

        game = int(input())

        while game != 0 and game != 1:
            game = int(input("Opção inválida, escolha uma das duas opções"))


def sobre():

    for i in range (espacos_de_diferenca):

        print("")

    print("Jogo produzido para o trabalho da turma de IPC (Introdução à programação de computadores")
    print("")
    print("Feito pela equipe de desenvolvedores:")
    print("")
    print("   Joao Vitor De Cordeiro Bentes Gonçalves")
    print("   Marcus Vinicius Paes da Silva Santos")
    print("   Nayara da Silva Cerdeira da Costa")
    print("   Luiz Daniel Raposo Nunes de Mello")
    print("   Felipe Eduardo Silva de Almeida")
    print("   Vitor Summer Oliveira Pantaleão")
    print("   Gabriel Barroso da Silva Lima")
    print("   Carlos Eduardo T. de Oliveira")
    print("   Diogo Roberto Duarte da Costa")
    print("   Evandro Padilha Barroso Filho")
    print("   Lucas Gabriel Silveira Duarte")
    print("   Adham Lucas da Silva Oliveira")
    print("   Yuri Leandro de Aquino Silva")
    print("   Roberta de Oliveira da Cruz")
    print("   Matheus de Oliveira Marques")
    print("   Jandinne Duarte de Oliveira")
    print("   Natália Cavalcante Xavier")
    print("   Enrique Leão Barbosa Izel")
    print("   Hugo Thadeu Silva Cardoso")
    print("   Ian Gabriel Costa Machado")
    print("   Gabriel de Queiroz Sousa")
    print("   Lukas Michel Souza Mota")
    print("   Tiago Ferreira Aranha")
    print("   Wesley da Silva Rocha")
    print("   Erik Atilio Silva Rey")
    print("   Vitor Simões Azevedo")
    print("   Edson de Lima Barros")
    print("   Judá Salazar Braga")
    print("   André Luis Laborda")
    print("   Luiz Paulo Machado")
    print("   Reinaldo Vargas")
    print("   Silas Castro")
    print("   Joelson Lima")
    print("   Fang Yao")
    print("")
    print("")
    print("")
    print("Todos os direitos reservados... kk to de zoas, isso é só um trabalho mesmo")
    print("")
    input("Pressione ENTER para voltar ao Menu")


sair = 0
espacos_de_diferenca = 40

while sair == 0:


    opcao = 5
    print("                   ╔════╕  ╔════╗ ╔═══╦══╗ ╔════╗  ╔════╗")
    print("                   ║      ║ ── ║ ║  ║  ║ ║    ║ ║    ║")
    print("                   ║      ╟────╢ ║  ║  ║ ╠════╝  ╟─────╢")
    print("                   ║      ║    ║ ║  ║  ║ ║      ║    ║")
    print("                   ╚════╛  ╜    ╙ ╜  ╨  ╙ ╜      ╚════╝")
    print("")
    print("               ╔═══╦══╗ ╒══╦══╕  ╔╗    ╓ ╔════╗ ╔═══╗  ╔═════╗")
    print("               ║  ║  ║    ║    ║╚╗   ║ ║ ── ║ ║ │ ╚╗ ║    ║")
    print("               ║  ║  ║    ║    ║ ╚╗  ║ ╟────╢ ║ ├─ ║ ╟─────╢")
    print("               ║  ║  ║    ║    ║  ╚╗ ║ ║    ║ ║ │ ╔╝ ║    ║")
    print("               ╜  ╨  ╙ ╘══╩══╛  ╜   ╚═╝ ╜    ╙ ╚═══╝  ╚═════╝")
    print("")
    print("")
    print("Modos de jogo:")
    print("")
    print("  jogar ----- 1")
    print("  sobre ----- 2")
    print("  sair ------ 3")
    print("")

    opcao = int(input("  sua opção: "))

    while opcao < 1 or opcao > 3:
        opcao = int(input("Comando inválido, digite um dos comandos mostrados no menu: "))

    if opcao == 1:

        jogo()

    elif opcao == 2:

        sobre()

    else:

        print("")
        print("Obrigado por jogar!")
        input("Pressione ENTER para sair")
        sair = 1