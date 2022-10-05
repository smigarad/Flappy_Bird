import sys
import pygame
from pygame.locals import *

class Game():
    def __init__(self):
        super().__init__()
        self.screen = (285, 500)
        self.display = pygame.display.set_mode(self.screen)
        self.run = 0
        self.fps = 30

    def Start(self):
        self.run = 1
        pygame.init()

    def Quit(self):
        self.run = 0
        pygame.quit()
        sys.exit()

    def Events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                self.Quit()

    def Draw(self,surface: pygame.Surface,pos: list):
        self.display.blit(surface,pos)