import os
import random


def montar_tabuleiro(linha, vetor):

    if linha == 1:

        for i in range(3):

            if vetor[i] == 0:

                print("║  ", i + 1, " ", end="")

            elif vetor[i] == 1:

                print("║   X  ", end="")

            else:

                print("║   O  ", end="")

    elif linha == 2:

        for i in range(3, 6):

            if vetor[i] == 0:

                print("║  ", i + 1, " ", end="")

            elif vetor[i] == 1:

                print("║   X  ", end="")

            else:

                print("║   O  ", end="")

    else:

        for i in range(6, 9):

            if vetor[i] == 0:

                print("║  ", i + 1, " ", end="")

            elif vetor[i] == 1:

                print("║   X  ", end="")

            else:

                print("║   O  ", end="")

    print("║")


def desenhar_tabuleiro(imagem):

    print("╔═══════╦═══════╦═══════╗")
    print("║      ║      ║      ║")

    montar_tabuleiro(1, imagem)

    print("║      ║      ║      ║")
    print("╠═══════╬═══════╬═══════╣")
    print("║      ║      ║      ║")

    montar_tabuleiro(2, imagem)

    print("║      ║      ║      ║")
    print("╠═══════╬═══════╬═══════╣")
    print("║      ║      ║      ║")

    montar_tabuleiro(3, imagem)

    print("║      ║      ║      ║")
    print("╚═══════╩═══════╩═══════╝")
    print("")


def dois_jogadores():
    game = 0

    while game == 0:

        tabuleiro = []
        jogo = 0
        jogadas = 0

        for i in range(9):
            tabuleiro.append(0)

        desenhar_tabuleiro(tabuleiro)

        jogador = 1

        while jogo == 0:

            if jogador == 1:

                i = int(input("Jogador 1, faça a escolha a posição do 'X': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 1
                jogadas += 1

                if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 1 or tabuleiro[3] == tabuleiro[4] == tabuleiro[
                    5] == 1 or tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 1 or tabuleiro[0] == tabuleiro[3] == \
                        tabuleiro[6] == 1 or tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 1 or tabuleiro[2] == \
                        tabuleiro[5] == tabuleiro[8] == 1 or tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 1 or \
                                                tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 1:

                    jogo = 1

                elif jogadas == 9:

                    jogo = 2

                else:

                    jogador = 2

            else:

                i = int(input("Jogador 2, faça a escolha a posição do 'O': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 2
                jogadas += 1

                if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 2 or tabuleiro[3] == tabuleiro[4] == tabuleiro[
                    5] == 2 or tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 2 or tabuleiro[0] == tabuleiro[3] == \
                        tabuleiro[6] == 2 or tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 2 or tabuleiro[2] == \
                        tabuleiro[5] == tabuleiro[8] == 2 or tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 2 or \
                                                tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 2:

                    jogo = 1

                elif jogadas == 9:

                    jogo = 2

                else:

                    jogador = 1

            desenhar_tabuleiro(tabuleiro)

        if jogo == 1:

            print("Jogador", jogador, "Ganhou!!!")

        else:

            print("Velha!")

        print("")
        print("Jogar novamente - 0 || Ir para menu - 1")

        game = int(input())

        while game != 0 and game != 1:
            game = int(input("Opção inválida, escolha uma das duas opções"))


def computador_facil():
    game = 0

    while game == 0:

        tabuleiro = []
        jogo = 0
        jogadas = 0

        for i in range(9):
            tabuleiro.append(0)

        desenhar_tabuleiro(tabuleiro)

        jogador = 1

        while jogo == 0:

            if jogador == 1:

                i = int(input("Jogador, faça a escolha a posição do 'X': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 1
                jogadas += 1

                if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 1 or tabuleiro[3] == tabuleiro[4] == tabuleiro[
                    5] == 1 or tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 1 or tabuleiro[0] == tabuleiro[3] == \
                        tabuleiro[6] == 1 or tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 1 or tabuleiro[2] == \
                        tabuleiro[5] == tabuleiro[8] == 1 or tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 1 or \
                                                tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 1:

                    jogo = 1

                elif jogadas == 9:

                    jogo = 2

                else:

                    jogador = 2

            else:

                i = random.randint(0, 8)

                while tabuleiro[i] != 0:

                    i = random.randint(0, 8)

                tabuleiro[i] = 2
                jogadas += 1

                if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 2 or tabuleiro[3] == tabuleiro[4] == tabuleiro[
                    5] == 2 or tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 2 or tabuleiro[0] == tabuleiro[3] == \
                        tabuleiro[6] == 2 or tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 2 or tabuleiro[2] == \
                        tabuleiro[5] == tabuleiro[8] == 2 or tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 2 or \
                                                tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 2:

                    jogo = 1

                elif jogadas == 9:

                    jogo = 2

                else:

                    jogador = 1

            desenhar_tabuleiro(tabuleiro)

        if jogo == 1:

            if jogador == 1:

                print("Você Venceu!!!")

            else:

                print("Você Perdeu!")

        else:

            print("Velha!")

        print("")
        print("Jogar novamente - 0 || Ir para menu - 1")

        game = int(input())

        while game != 0 and game != 1:
            game = int(input("Opção inválida, escolha uma das duas opções"))


def computador_dificil():
    game = 0

    while game == 0:

        tabuleiro = []
        jogo = 0  # jogo == 1: perdeu || jogo == 2: velhou

        for i in range(9):
            tabuleiro.append(0)

        tabuleiro[8] = 2

        desenhar_tabuleiro(tabuleiro)

        i = int(input("Jogador, faça a escolha a posição do 'X': "))

        while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
            i = int(input("Jogada inválida, escolha uma posição válida: "))

        tabuleiro[i - 1] = 1
        desenhar_tabuleiro(tabuleiro)

        # linha 1 de possibilidade

        if i == 2 or i == 8:

            tabuleiro[2] = 2
            desenhar_tabuleiro(tabuleiro)

            i = int(input("Jogador, faça a escolha a posição do 'X': "))

            while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                i = int(input("Jogada inválida, escolha uma posição válida: "))

            tabuleiro[i - 1] = 1
            desenhar_tabuleiro(tabuleiro)

            if i != 6:

                tabuleiro[5] = 2
                desenhar_tabuleiro(tabuleiro)

                jogo = 1

            else:

                tabuleiro[4] = 2
                desenhar_tabuleiro(tabuleiro)

                i = int(input("Jogador, faça a escolha a posição do 'X': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 1
                desenhar_tabuleiro(tabuleiro)

                if i == 1:

                    tabuleiro[6] = 2
                    desenhar_tabuleiro(tabuleiro)

                    jogo = 1

                else:

                    tabuleiro[0] = 2
                    desenhar_tabuleiro(tabuleiro)

                    jogo = 1

        # linha 1 de possibilidade

        # linha 2 de possibilidade

        elif i == 6 or i == 4:

            tabuleiro[6] = 2
            desenhar_tabuleiro(tabuleiro)

            i = int(input("Jogador, faça a escolha a posição do 'X': "))

            while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                i = int(input("Jogada inválida, escolha uma posição válida: "))

            tabuleiro[i - 1] = 1
            desenhar_tabuleiro(tabuleiro)

            if i != 8:

                tabuleiro[7] = 2
                desenhar_tabuleiro(tabuleiro)

                jogo = 1

            else:

                tabuleiro[4] = 2
                desenhar_tabuleiro(tabuleiro)

                i = int(input("Jogador, faça a escolha a posição do 'X': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 1
                desenhar_tabuleiro(tabuleiro)

                if i == 1:

                    tabuleiro[2] = 2
                    desenhar_tabuleiro(tabuleiro)

                    jogo = 1

                else:

                    tabuleiro[0] = 2
                    desenhar_tabuleiro(tabuleiro)

                    jogo = 1

        # linha 2 de possibilidade

        # linha 3 de possibilidade

        elif i == 1:

            tabuleiro[6] = 2
            desenhar_tabuleiro(tabuleiro)

            i = int(input("Jogador, faça a escolha a posição do 'X': "))

            while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                i = int(input("Jogada inválida, escolha uma posição válida: "))

            tabuleiro[i - 1] = 1
            desenhar_tabuleiro(tabuleiro)

            if i != 8:

                tabuleiro[7] = 2
                desenhar_tabuleiro(tabuleiro)

                jogo = 1

            else:

                tabuleiro[2] = 2
                desenhar_tabuleiro(tabuleiro)

                i = int(input("Jogador, faça a escolha a posição do 'X': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 1
                desenhar_tabuleiro(tabuleiro)

                if i != 5:

                    tabuleiro[4] = 2
                    desenhar_tabuleiro(tabuleiro)

                    jogo = 1

                else:

                    tabuleiro[5] = 2
                    desenhar_tabuleiro(tabuleiro)

                    jogo = 1

        # linha 3 de possibilidade

        # linha 4 de possibilidade

        elif i == 5:

            tabuleiro[0] = 2
            desenhar_tabuleiro(tabuleiro)

            i = int(input("Jogador, faça a escolha a posição do 'X': "))

            while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                i = int(input("Jogada inválida, escolha uma posição válida: "))

            tabuleiro[i - 1] = 1
            desenhar_tabuleiro(tabuleiro)

            if i == 3:

                tabuleiro[6] = 2
                desenhar_tabuleiro(tabuleiro)

                i = int(input("Jogador, faça a escolha a posição do 'X': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 1
                desenhar_tabuleiro(tabuleiro)

                if i == 4:

                    tabuleiro[7] = 2
                    desenhar_tabuleiro(tabuleiro)

                else:

                    tabuleiro[3] = 2
                    desenhar_tabuleiro(tabuleiro)

                jogo = 1

            elif i == 7:

                tabuleiro[2] = 2
                desenhar_tabuleiro(tabuleiro)

                i = int(input("Jogador, faça a escolha a posição do 'X': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 1
                desenhar_tabuleiro(tabuleiro)

                if i == 2:

                    tabuleiro[5] = 2
                    desenhar_tabuleiro(tabuleiro)

                else:

                    tabuleiro[1] = 2
                    desenhar_tabuleiro(tabuleiro)

                jogo = 1

            elif i == 2:

                tabuleiro[7] = 2
                desenhar_tabuleiro(tabuleiro)

                i = int(input("Jogador, faça a escolha a posição do 'X': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 1
                desenhar_tabuleiro(tabuleiro)

                if i != 7:

                    tabuleiro[6] = 2
                    desenhar_tabuleiro(tabuleiro)

                    jogo = 1

                else:

                    tabuleiro[2] = 2
                    desenhar_tabuleiro(tabuleiro)

                    i = int(input("Jogador, faça a escolha a posição do 'X': "))

                    while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                        i = int(input("Jogada inválida, escolha uma posição válida: "))

                    tabuleiro[i - 1] = 1
                    desenhar_tabuleiro(tabuleiro)

                    if i == 6:

                        tabuleiro[3] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 2

                    else:

                        tabuleiro[5] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 1

            elif i == 6:

                tabuleiro[3] = 2
                desenhar_tabuleiro(tabuleiro)

                i = int(input("Jogador, faça a escolha a posição do 'X': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 1
                desenhar_tabuleiro(tabuleiro)

                if i != 7:

                    tabuleiro[6] = 2
                    desenhar_tabuleiro(tabuleiro)

                    jogo = 1

                else:

                    tabuleiro[2] = 2
                    desenhar_tabuleiro(tabuleiro)

                    i = int(input("Jogador, faça a escolha a posição do 'X': "))

                    while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                        i = int(input("Jogada inválida, escolha uma posição válida: "))

                    tabuleiro[i - 1] = 1
                    desenhar_tabuleiro(tabuleiro)

                    if i == 2:

                        tabuleiro[1] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 2

                    else:

                        tabuleiro[7] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 1

            elif i == 4:

                tabuleiro[5] = 2
                desenhar_tabuleiro(tabuleiro)

                i = int(input("Jogador, faça a escolha a posição do 'X': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 1
                desenhar_tabuleiro(tabuleiro)

                if i != 3:

                    tabuleiro[2] = 2
                    desenhar_tabuleiro(tabuleiro)

                    jogo = 1

                else:

                    tabuleiro[6] = 2
                    desenhar_tabuleiro(tabuleiro)

                    i = int(input("Jogador, faça a escolha a posição do 'X': "))

                    while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                        i = int(input("Jogada inválida, escolha uma posição válida: "))

                    tabuleiro[i - 1] = 1
                    desenhar_tabuleiro(tabuleiro)

                    if i == 8:

                        tabuleiro[1] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 2

                    else:

                        tabuleiro[7] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 1

            else:

                tabuleiro[1] = 2
                desenhar_tabuleiro(tabuleiro)

                i = int(input("Jogador, faça a escolha a posição do 'X': "))

                while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                    i = int(input("Jogada inválida, escolha uma posição válida: "))

                tabuleiro[i - 1] = 1
                desenhar_tabuleiro(tabuleiro)

                if i != 3:

                    tabuleiro[2] = 2
                    desenhar_tabuleiro(tabuleiro)

                    jogo = 1

                else:

                    tabuleiro[6] = 2
                    desenhar_tabuleiro(tabuleiro)

                    i = int(input("Jogador, faça a escolha a posição do 'X': "))

                    while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                        i = int(input("Jogada inválida, escolha uma posição válida: "))

                    tabuleiro[i - 1] = 1
                    desenhar_tabuleiro(tabuleiro)

                    if i == 4:

                        tabuleiro[5] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 2

                    else:

                        tabuleiro[3] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 1

        # linha 4 de possibilidade

        # linha 5 de possibilidade

        else:

            tabuleiro[0] = 2
            desenhar_tabuleiro(tabuleiro)

            i = int(input("Jogador, faça a escolha a posição do 'X': "))

            while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                i = int(input("Jogada inválida, escolha uma posição válida: "))

            tabuleiro[i - 1] = 1
            desenhar_tabuleiro(tabuleiro)

            if i != 5:

                tabuleiro[4] = 2
                desenhar_tabuleiro(tabuleiro)

                jogo = 1

            else:

                if tabuleiro[2] == 1:

                    tabuleiro[6] = 2
                    desenhar_tabuleiro(tabuleiro)

                    i = int(input("Jogador, faça a escolha a posição do 'X': "))

                    while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                        i = int(input("Jogada inválida, escolha uma posição válida: "))

                    tabuleiro[i - 1] = 1
                    desenhar_tabuleiro(tabuleiro)

                    if i == 4:

                        tabuleiro[7] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 1

                    else:

                        tabuleiro[3] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 1

                else:

                    tabuleiro[2] = 2
                    desenhar_tabuleiro(tabuleiro)

                    i = int(input("Jogador, faça a escolha a posição do 'X': "))

                    while i < 1 or i > 9 or tabuleiro[i - 1] != 0:
                        i = int(input("Jogada inválida, escolha uma posição válida: "))

                    tabuleiro[i - 1] = 1
                    desenhar_tabuleiro(tabuleiro)

                    if i == 2:

                        tabuleiro[5] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 1

                    else:

                        tabuleiro[1] = 2
                        desenhar_tabuleiro(tabuleiro)

                        jogo = 1

        # linha 5 de possibilidade

        if jogo == 1:

            print("Você perdeu!")

        else:

            print("Velhou!")

        print("")
        print("Jogar novamente - 0 || Ir para menu - 1")

        game = int(input())

        while game != 0 and game != 1:
            game = int(input("Opção inválida, escolha uma das duas opções"))


def sobre():

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


while sair == 0:

    opcao = 5
    print("                   ╒══╦══╕ ╔════╗ ╔════╕ ╔════╗")
    print("                      ║   ║   ║ ║      ║    ║")
    print("                      ║   ╟────╢ ║  ──╥ ╟────╢")
    print("                      ║   ║   ║ ║    ║ ║    ║")
    print("                   ╘══╝   ╚════╝ ╚════╝  ╚════╝")
    print("")
    print("                           ┌───┐  ┌────┐")
    print("                           │ │ └┐ │ ── │")
    print("                           │ ├─ │ ├────┤")
    print("                           │ │ ┌┘ │    │")
    print("                           └───┘  ┘    └")
    print("")
    print("               ╖    ╓  ╔════╕  ╖     ╖     ╓ ╔════╗")
    print("               ║    ║  ║      ║      ║    ║ ║ ── ║")
    print("               ║    ║  ╟────  ║      ╟─────╢ ╟────╢")
    print("               ╚╗  ╔╝  ║      ║      ║    ║ ║    ║")
    print("                ╚══╝   ╚════╛  ╚════╛ ╜     ╙ ╜    ╙")
    print("")
    print("")
    print("Modos de jogo:")
    print("")
    print("  dois jogadores ----- 1")
    print("  computador fácil --- 2")
    print("  computador difícil - 3")
    print("  sobre -------------- 4")
    print("  sair --------------- 5")
    print("")

    opcao = int(input("  sua opção: "))

    while opcao < 1 or opcao > 5:
        opcao = int(input("Comando inválido, digite um dos comandos mostrados no menu: "))

    if opcao == 1:

        dois_jogadores()

    elif opcao == 2:

        computador_facil()

    elif opcao == 3:

        computador_dificil()

    elif opcao == 4:

        sobre()

    else:

        print("")
        print("Obrigado por jogar!")
        input("Pressione ENTER para sair")
        sair = 1