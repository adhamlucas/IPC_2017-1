import pygame, sys
from pygame.locals import *

# inicia o pygame
pygame.init()

# atalho para cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# inicia a janela
tela = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Hello world!")


# inicia as fontes
basicFont = pygame.font.SysFont("Times New Roman", 48)

# inicia o texto
text = basicFont.render("TIAGO", True, WHITE, BLUE)
textRect = text.get_rect()
print(textRect)
textRect.centerx = tela.get_rect().centerx
textRect.centery = tela.get_rect().centery


# desenha o fundo branco
tela.fill(WHITE)

# desenha um poligono verde na superficie
poligono = pygame.draw.polygon(tela, GREEN, ((146, 0), (291, 106), (236, 277),
                                           (56, 277), (0, 106)))

# desenha algumas linhas azuis na superficie
linha1 = pygame.draw.line(tela, BLUE, (60, 60), (120, 60), 10)
linha2 = pygame.draw.line(tela, BLUE, (120, 60), (60, 120))
linha3 = pygame.draw.line(tela, BLUE, (60, 120), (120, 120), 4)

# desenha um circulo azul na superficie
circulo = pygame.draw.circle(tela, BLUE, (300, 50), 20, 0)

# desenha uma elipse vermelha na superficie
elipse = pygame.draw.ellipse(tela, RED, (100, 250, 400, 80), 1)

# desenha o retangulo do fundo do texto na superficie
retangulo = pygame.draw.rect(tela, RED, (textRect.left - 20, textRect.top - 20,
                                      textRect.width + 40, textRect.height + 40))

# obtem um array de pixel da superficie
pixArray = pygame.PixelArray(tela)
pixArray[480][380] = BLACK
del pixArray

# desenha o texto na janela
tela.blit(text, textRect)

# verifica se objetos tem intersecção - retorna 1 para True e 0 para False
colisao = circulo.colliderect( poligono )

# desenha a janela na tela
pygame.display.update()

pygame.time.delay(2000)

retangulo.move_ip(40,50)
block = pygame.draw.rect(tela, RED, retangulo, 0)
retangulo.move(40,50)
pygame.display.update()

# rodaoloopdojogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

sys.exit()
