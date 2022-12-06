import pygame, sys, os
from random import randint
import random
from math import ceil

pygame.init()
FPS = 60
clock = pygame.time.Clock()

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

class Word(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(FONT, 24)
        self.word = self.font.render(self.change(), True, PINK)
        self.rect_width = ceil(self.word.get_width() / 2)
        self.rect = self.word.get_rect()
        self.rect.center = (random.randint(self.rect_width, WIDTH - self.rect_width), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.bottom > 600:
            self.word = self.font.render(self.change(), True, PINK)
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect_width, WIDTH - self.rect_width), 0)

    def draw(self, surface):
        surface.blit(self.word, self.rect)

    def change(self):
        self.list_words = ["Cachorro", "Gato", "Camelo", "Arara", "Unicórnio", "Dinossauro", "Leão"]
        self.text = random.choice(self.list_words)

        return self.text

running = True

W1 = Word()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    W1.move()
    SCREEN.fill(BLACK)

    W1.draw(SCREEN)

    pygame.display.flip()
    clock.tick(FPS)
