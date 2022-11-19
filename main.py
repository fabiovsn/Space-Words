import random
import pygame, sys, os
from random import randint

pygame.init()

# Janela
SIZE = WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode(SIZE)

# Cores
BLACK = (0, 0, 0)
PINK = (234, 212, 252)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# Fontes
DIRECTORY = os.getcwd()
FONT = DIRECTORY + "/fonts/unispace_rg.ttf"

pygame.display.set_caption("Shooting Words")

class Text(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        list_words = ["cachorro", "planta", "arvore"]
        self.text = random.choice(list_words)
        #self.text = "Cachorro"
        self.font = pygame.font.Font(FONT, 24)
        self.text_render = self.font.render(self.text, True, PINK)
        self.pos_x = randint(0, 100)
        self.pos_y = randint(0, 100)
        self.rect = self.text_render.get_rect()

        pygame.time.wait(2000)

clock = pygame.time.Clock()

text = Text()

x = text.pos_x
y = text.pos_y

running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # atualiza tela
    pygame.display.flip()

    SCREEN.fill(BLACK)

    SCREEN.blit(text.text_render, (x, y))

    y += 1