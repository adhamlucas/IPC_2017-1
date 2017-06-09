import pygame
from pygame import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.font.init()

fonte30 = pygame.font.SysFont('Comic Sans MS', 30)
fonte50 = pygame.font.SysFont('Comic Sans MS', 50)


def play(caminho_arquivo):
    pygame.mixer.music.load(caminho_arquivo)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()


def mensagem(texto):
    textsurface = fonte30.render(texto, 1, WHITE)
    tela.blit(textsurface, (10, 600))


def limpar_mensagens():
    pygame.draw.rect(tela, BLACK, (10, 600, 600, 50))
    pygame.display.update()


def finaliza(texto):
    fundo = pygame.image.load("img/fundo.png").convert_alpha()
    tela.blit(fundo, pygame.rect.Rect(0, 0, 128, 128))
    pygame.display.flip()
    text = fonte50.render(texto, 1, WHITE)
    text_rect = text.get_rect()
    tela.blit(text, [100, 250])


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


def abertura():
    pygame.mixer.music.load(jogo_inicio)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(0)
    textsurface = fonte50.render("JOGO DA VELHA", 1, WHITE)
    tela.blit(textsurface, (int(quadrante[0] / 2) + 0, int(quadrante[1]) + 140))

    for i in range(1, 25):
        tela.blit(pygame.image.load('img/capcom' + str(i) + '.png'),
                  (int(quadrante[0] / 2) + 50, int(quadrante[1]) + 50))
        pygame.time.delay(100)
        pygame.display.flip()

    pygame.time.delay(1000)


tamanho_tela = (600, 650)
tamanho_tabuleiro = (600, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Jogo da Velha Beta")
tela.fill(BLACK)
quadrante = (int(tamanho_tabuleiro[0] / 3), int(tamanho_tabuleiro[1] / 3))

jogada_certa = 'audio/jogada_certa.mp3'
jogada_errada = 'audio/jogada_errada.mp3'
jogo_inicio = 'audio/capcom.mp3'
jogo_perdeu = 'audio/jogo_perdeu.mp3'
jogo_ganhou = 'audio/jogo_ganhou.mp3'

abertura()

x = pygame.image.load("img/x.png")
o = pygame.image.load("img/o.png")
x = pygame.transform.scale(x, quadrante)
o = pygame.transform.scale(o, quadrante)

tabuleiro = pygame.Surface(tamanho_tabuleiro)
tabuleiro.fill(WHITE)

pygame.draw.rect(tabuleiro, BLACK, ((tamanho_tabuleiro[1] / 3), 0, 5, tamanho_tabuleiro[1]))
pygame.draw.rect(tabuleiro, BLACK, ((tamanho_tabuleiro[1] / 3) * 2, 0, 5, tamanho_tabuleiro[1]))
pygame.draw.rect(tabuleiro, BLACK, (0, (tamanho_tabuleiro[0] / 3), tamanho_tabuleiro[0], 5))
pygame.draw.rect(tabuleiro, BLACK, (0, (tamanho_tabuleiro[0] / 3) * 2, tamanho_tabuleiro[0], 5))

posicoes_tabuleiro = [
    [0, 0, 0], [quadrante[0], 0, 0], [2 * quadrante[0], 0, 0],
    [0, quadrante[1], 0], [quadrante[0], quadrante[1], 0], [2 * quadrante[0], quadrante[1], 0],
    [0, 2 * quadrante[1], 0], [quadrante[0], 2 * quadrante[1], 0], [2 * quadrante[0], 2 * quadrante[1], 0]
]

tela.blit(tabuleiro, (0, 0))

pygame.display.flip()

jogadas = [["X", []], ["O", []]]

jogador = ("X", "O")

jogada = 0

vez = jogador[0]
mensagem("Vez de Jogar: " + vez)

done = False

while not done:

    position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
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
