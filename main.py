import random

import pygame, sys, os
import pygame.freetype
from math import ceil
from itertools import cycle

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
        self.list = ["Cachorro", "Gato", "Camelo", "Arara", "Unicórnio", "Dinossauro", "Leão"]
        self.current = random.choice(self.list)
        self.current_idx = 0  # points to the current letter, as you have already guessed
        self.font = pygame.freetype.Font(FONT, 24)
        self.font.origin = True
        self.M_ADV_X = 4
        self.text_surf_rect = self.font.get_rect(self.current)
        self.baseline = self.text_surf_rect.y
        self.text_surf = pygame.Surface(self.text_surf_rect.size)
        self.rect_width = ceil(self.text_surf.get_width()/2)
        self.text_surf_rect.center = (random.randint(self.rect_width, WIDTH - self.rect_width), 0)
        self.metrics = self.font.get_metrics(self.current)

    def move(self):
        self.text_surf_rect.move_ip(0, 2)

        events = pygame.event.get()

        for e in events:
            if e.type == pygame.QUIT:
                return

            if e.type == pygame.KEYDOWN:
                if e.unicode == self.current[self.current_idx].lower():
                    # if we press the correct letter, move the index
                    self.current_idx += 1
                    if self.current_idx >= len(self.current):
                        self.text_surf_rect.top = 0
                        self.current = self.change()
                        self.current_idx = 0
                        self.text_surf_rect = self.font.get_rect(self.current)
                        self.baseline = self.text_surf_rect.y
                        self.text_surf = pygame.Surface(self.text_surf_rect.size)
                        self.text_surf_rect.center = (random.randint(self.rect_width, WIDTH - self.rect_width), 0)
                        self.metrics = self.font.get_metrics(self.current)

        SCREEN.fill(BLACK)
        self.text_surf.fill(BLACK)

        x = 0
        # render each letter of the current sentence one by one
        for (idx, (letter, metric)) in enumerate(zip(self.current, self.metrics)):
            # select the right color
            if idx == self.current_idx:
                color = RED
            elif idx < self.current_idx:
                color = BLACK
            else:
                color = PINK

            # render the single letter
            self.font.render_to(self.text_surf, (x, self.baseline), letter, color)
            # and move the start position
            x += metric[self.M_ADV_X]

        SCREEN.blit(self.text_surf, self.text_surf_rect)
        pygame.display.flip()

    def change(self):
        self.text = random.choice(self.list)
        return self.text

pygame.init()

running = True

W1 = Word()

while running:

    W1.move()
    clock.tick(FPS)