import pygame
from pygame.locals import *

class Background_Assets():
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load(
            "assets/sprites/background-night.png")
        self.floor = pygame.image.load("assets/sprites/base.png")
        pygame.display.set_caption("Flappy bird")
        self.icon = pygame.image.load("assets/favicon.ico")
        pygame.display.set_icon(self.icon)
        self.gameover = pygame.image.load("assets/sprites/gameover.png")

    def Draw(self, display: pygame.Surface, screen: list):
        display.blit(self.background, (0, 0))
        display.blit(self.floor, (0, 450))