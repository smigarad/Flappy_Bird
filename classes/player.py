import sys
import pygame
import time
from pygame.locals import *
from classes.score import Score


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            "assets/sprites/yellowbird-downflap.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.isJump = False
        self.jumpCount = 12
        self.count = 0
        self.score = Score()
        self.rotation = 0
        self.rotaiton_speed = 2

    def move(self):
        if self.rect.y >= 430:
            self.rect.y = 430
        elif self.rect.y < 0:
            self.rect.y = 0
        else:
            self.rect.move_ip(0, 4)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -12:
                neg = 1
            if self.jumpCount < 0:
                neg = 1
            self.rect.y -= self.jumpCount ** 2 * 0.1 * neg
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 12

    def Keys(self):
        keys = pygame.key.get_pressed()
        if keys[K_q]:
            time.sleep(1)
            pygame.quit()
            sys.exit()

        if keys[K_SPACE]:  # retarded jump system
            if self.count > 17:
                self.isJump = False
            else:
                self.isJump = True
                self.count += 1

        if self.isJump == False:
            self.count = 0

    def fall(self):
        self.rect.y += self.rect.y**0.3
    
    def Rotate(self):
        #while self.rect.y>= screen[1] + 20:
        if self.rotation <88:
             self.rotation  = ( self.rotation  +self.rotaiton_speed) %90
        surface = pygame.transform.rotate(self.image,-self.rotation)
        return surface