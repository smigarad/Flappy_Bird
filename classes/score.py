import pygame
from pygame.locals import *

class Score():
    def __init__(self):
        super().__init__()
        self.score = 0

    def LoadScore(self,score : int):
        return pygame.image.load(f"assets/sprites/{score}.png")

    def PrintScore(self, display: pygame.Surface, screen: list):
        if self.score > 9:
            score_last_digit = self.score % 10
            score_first_digit = self.score // 10
        else:
            score_img = self.LoadScore(self.score)

        if self.score < 10:
            display.blit(score_img, (screen[0] / 2 - 10, 100))

        elif self.score < 100:
            score_img = self.LoadScore(score_first_digit)
            display.blit(score_img, (screen[0] / 2 - 25, 100))
            score_img = self.LoadScore(score_last_digit)
            display.blit(score_img, (screen[0] / 2 - 5, 100))