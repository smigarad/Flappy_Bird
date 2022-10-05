import pygame
import random
from pygame.locals import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/pipe-green.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, 300), random.choice([0, 500]))
        self.speed = 2

    def move(self):
        self.rect.move_ip(-self.speed, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)