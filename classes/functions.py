import pygame
import random
import time
from pygame.locals import *
from classes.game import Game
from classes.background_assets import Background_Assets
from classes.sounds import Sounds
from classes.player import Player
from classes.obstacle import Obstacle

def Spawn(obstacle_upper: Obstacle, obstacle_lower: Obstacle,choices: list, init : bool):
    if init or obstacle_upper.rect.x == -70:

        choice = choices.pop()
        choices.insert(0,choice)

        if choice == 4:
            random_x = 700
        if choice == 5:
            random_x = 500
        if choice == 6:
            random_x = 300

        random_y = random.randint(0, 150)
        obstacle_upper.rect.center = (random_x, 400 + random_y)
        obstacle_lower.rect.center = (random_x, 0 + random_y)

def Spawn_Control(obstacles:pygame.sprite.Group):
    sum = obstacles.sprites()[1].rect.x  - obstacles.sprites()[0].rect.x   
    if sum <= 200 and sum >= 0:
        obstacles.sprites()[1].rect.x += 200 - sum
        obstacles.sprites()[4].rect.x += 200 - sum
    sum= obstacles.sprites()[2].rect.x  - obstacles.sprites()[1].rect.x
    if sum <= 200 and sum >= 0:
        obstacles.sprites()[2].rect.x += 200 - sum
        obstacles.sprites()[5].rect.x += 200 - sum
    sum= obstacles.sprites()[2].rect.x  - obstacles.sprites()[0].rect.x
    if sum <= 200 and sum >= 0:
        obstacles.sprites()[2].rect.x += 200 - sum
        obstacles.sprites()[5].rect.x += 200 - sum
    sum = obstacles.sprites()[0].rect.x  - obstacles.sprites()[2].rect.x
    if sum <= 200 and sum >= 0:
        obstacles.sprites()[0].rect.x += 200 - sum
        obstacles.sprites()[3].rect.x += 200 - sum
    sum = obstacles.sprites()[1].rect.x  - obstacles.sprites()[2].rect.x
    if sum <= 200 and sum >= 0:
        obstacles.sprites()[1].rect.x += 200 - sum
        obstacles.sprites()[4].rect.x += 200 - sum
    sum = obstacles.sprites()[0].rect.x  - obstacles.sprites()[1].rect.x
    if sum <= 200 and sum >= 0:
        obstacles.sprites()[0].rect.x += 200 - sum
        obstacles.sprites()[3].rect.x += 200 - sum
        


def GameEnd(obstacles:pygame.sprite.Group, player: Player, game: Game, sounds: Sounds, assets:Background_Assets, fps : int,framespersec :pygame.time.Clock):
    sounds.hit.play()
    time.sleep(0.5)
    sounds.die.play()
    
    while player.rect.y <=game.screen[1] +20:
        player.fall()
        game.Draw(assets.background,(0,0))
        game.Draw(player.Rotate(), player.rect)
        obstacles.draw(game.display)
        player.score.PrintScore(game.display,game.screen)
        game.Draw(assets.gameover,(40,200))
        game.Draw(assets.floor,(0,450))
        pygame.display.update()
        framespersec.tick(fps)
    game.Draw(assets.gameover,(40,200))
    pygame.display.update()
    game.Quit()