import pygame
from pygame.locals import *

class Sounds():
    def __init__(self):
        super().__init__()
        self.wing = pygame.mixer.Sound("assets/audio/wing.wav")
        self.die = pygame.mixer.Sound("assets/audio/die.wav")
        self.point = pygame.mixer.Sound("assets/audio/point.wav")
        self.hit = pygame.mixer.Sound("assets/audio/hit.wav")
