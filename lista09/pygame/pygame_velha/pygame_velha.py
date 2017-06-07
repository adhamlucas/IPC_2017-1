# Jogo da velha

import pygame
from pygame import *

# inicia biblioteca pygame
pygame.init()

# Definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# inicia biblioteca de fontes (texto)
pygame.font.init()

# cria formatação específica para textos
fonte30 = pygame.font.SysFont('Comic Sans MS', 30)
fonte50 = pygame.font.SysFont('Comic Sans MS', 50)


######## FUNÇÕES DO JOGO ##########

# função que toca arquivo de som
def play(caminho_arquivo):
    pygame.mixer.music.load(caminho_arquivo)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()


# função para imprimir mensagem na área de notificações
def mensagem(texto):
    textsurface = fonte30.render(texto, 1, WHITE)
    tela.blit(textsurface, (10, 600))


# função para limpar mensagens na área de notificações
def limpar_mensagens():
    pygame.draw.rect(tela, BLACK, (10, 600, 600, 50))
    pygame.display.update()


# função que finaliza o jogo
def finaliza(texto):
    fundo = pygame.image.load("img/fundo.png").convert_alpha()
    tela.blit(fundo, pygame.rect.Rect(0, 0, 128, 128))
    pygame.display.flip()
    text = fonte50.render(texto, 1, WHITE)
    text_rect = text.get_rect()
    tela.blit(text, [100, 250])


# funcao que verifica se algum jogador ganhou
def verifica_se_ganhou(jogada):
    vitorias_possiveis = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for j in vitorias_possiveis:
        vezes = 0
        for l in j:
            for i in jogada:

                if l == i:
                    vezes += 1

        if vezes == 3:
            break

    if vezes == 3:
        return True
    else:
        return False


# tamanho_tela de abertura do jogo
def abertura():
    # música
    pygame.mixer.music.load(jogo_inicio)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(0)

    # titulo
    textsurface = fonte50.render("JOGO DA VELHA", 1, WHITE)
    tela.blit(textsurface, (int(quadrante[0] / 2) + 0, int(quadrante[1]) + 140))

    # animação capcom
    for i in range(1, 25):
        tela.blit(pygame.image.load('img/capcom' + str(i) + '.png'),
                  (int(quadrante[0] / 2) + 50, int(quadrante[1]) + 50))
        pygame.time.delay(100)
        pygame.display.flip()

    pygame.time.delay(1000)


# tamanho da janela
tamanho_tela = (600, 650)

# tamanho do tabuleiro
tamanho_tabuleiro = (600, 600)

tela = pygame.display.set_mode(tamanho_tela)

# Nome do Jogo (barra de título) e cor do fundo
pygame.display.set_caption("Jogo da Velha Beta")
tela.fill(BLACK)

# dimensoes de cada quadrante no tabuleiro
quadrante = (int(tamanho_tabuleiro[0] / 3), int(tamanho_tabuleiro[1] / 3))

# efeitos sonoros
jogada_certa = 'audio/jogada_certa.mp3'
jogada_errada = 'audio/jogada_errada.mp3'
jogo_inicio = 'audio/capcom.mp3'
jogo_perdeu = 'audio/jogo_perdeu.mp3'
jogo_ganhou = 'audio/jogo_ganhou.mp3'

# inicia abertura do jogo
abertura()

# imagem dos jogadores
x = pygame.image.load("img/x.png")
o = pygame.image.load("img/o.png")
# ajustando tamanho da imagem para o tamanho d quadrante
x = pygame.transform.scale(x, quadrante)
o = pygame.transform.scale(o, quadrante)

# cria tabuleiro (surface)
tabuleiro = pygame.Surface(tamanho_tabuleiro)
# cor de fundo do tabuleiro
tabuleiro.fill(WHITE)

# ------- desenho das linhas do tabueiro --------
pygame.draw.rect(tabuleiro, BLACK, ((tamanho_tabuleiro[1] / 3), 0, 5, tamanho_tabuleiro[1]))
pygame.draw.rect(tabuleiro, BLACK, ((tamanho_tabuleiro[1] / 3) * 2, 0, 5, tamanho_tabuleiro[1]))
pygame.draw.rect(tabuleiro, BLACK, (0, (tamanho_tabuleiro[0] / 3), tamanho_tabuleiro[0], 5))
pygame.draw.rect(tabuleiro, BLACK, (0, (tamanho_tabuleiro[0] / 3) * 2, tamanho_tabuleiro[0], 5))

# posições ([x,y]) possíveis no tabuleiro - para incluir o X e o O
posicoes_tabuleiro = [
    # primeira linha
    [0, 0, 0], [quadrante[0], 0, 0], [2 * quadrante[0], 0, 0],
    # segunda linha
    [0, quadrante[1], 0], [quadrante[0], quadrante[1], 0], [2 * quadrante[0], quadrante[1], 0],
    # terceira linha
    [0, 2 * quadrante[1], 0], [quadrante[0], 2 * quadrante[1], 0], [2 * quadrante[0], 2 * quadrante[1], 0]
]

# adiciona o tabuleiro (testes)
tela.blit(tabuleiro, (0, 0))
# atualiza display com o tabuleiro
pygame.display.flip()

# tabela que armazena as jogadas
jogadas = [["X", []], ["O", []]]

# nomes dos jogadores
jogador = ("X", "O")

# contador de jogadas - para saber quando termina (no cado de velhar)
jogada = 0

# variável que guarda o jogador de quem vai jogar
vez = jogador[0]
mensagem("Vez de Jogar: " + vez)

# Loop de eventos
done = False

# -------- Loop de eventos -----------
while not done:

    # posição do mouse
    position = pygame.mouse.get_pos()

    # --- Loop principal
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # lê posição e grava X ou O
            for i in range(len(posicoes_tabuleiro)):

                if posicoes_tabuleiro[i][0] < position[0] < posicoes_tabuleiro[i][0] + quadrante[0] and \
                                        posicoes_tabuleiro[i][1] < position[1] < posicoes_tabuleiro[i][1] + \
                                quadrante[
                                    1]:

                    limpar_mensagens()
                    jogada += 1

                    if posicoes_tabuleiro[i][2] == 1:
                        play(jogada_errada)
                        mensagem('Posição Ocupada! Jogue numa vazia!')

                    else:

                        if vez == jogador[0]:

                            posicoes_tabuleiro[i][2] = 1
                            tela.blit(x, (posicoes_tabuleiro[i][0], posicoes_tabuleiro[i][1]))
                            jogadas[1][1].append(i)

                            if verifica_se_ganhou(jogadas[1][1]):
                                finaliza("Vencedor: " + vez)
                                play(jogo_ganhou)

                            else:
                                if jogada == 9:
                                    finaliza("VELHOU!")
                                    play(jogo_perdeu)
                                else:
                                    vez = jogador[1]
                                    mensagem("Vez de Jogar: " + vez)
                                    play(jogada_certa)

                        else:

                            posicoes_tabuleiro[i][2] = 1
                            tela.blit(o, (posicoes_tabuleiro[i][0], posicoes_tabuleiro[i][1]))

                            jogadas[0][1].append(i)

                            if verifica_se_ganhou(jogadas[0][1]):
                                finaliza("Vencedor: " + vez)
                                play(jogo_ganhou)

                            else:
                                if jogada == 9:
                                    finaliza("VELHOU!")
                                    play(jogo_perdeu)
                                else:
                                    vez = jogador[0]
                                    mensagem(" Vez de Jogar: " + vez)
                                    play(jogada_certa)

                    pygame.display.flip()

pygame.quit()