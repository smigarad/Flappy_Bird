import pygame
from pygame.locals import *
from classes.game import Game
from classes.background_assets import Background_Assets
from classes.sounds import Sounds
from classes.player import Player
from classes.obstacle import Obstacle
from classes.functions import *

# main func
def main():
    # init all objects
    game = Game()
    game.Start()
    assets = Background_Assets()
    framespersec = pygame.time.Clock()
    player = Player()
    sounds = Sounds()

    obstacle_lower0 = Obstacle()
    obstacle_lower0.image = pygame.transform.flip(
        obstacle_lower0.image, False, True)
    obstacle_lower1 = Obstacle()
    obstacle_lower1.image = pygame.transform.flip(
        obstacle_lower1.image, False, True)
    obstacle_lower2 = Obstacle()
    obstacle_lower2.image = pygame.transform.flip(
        obstacle_lower2.image, False, True)

    obstacle_upper0 = Obstacle()
    obstacle_upper1 = Obstacle()
    obstacle_upper2 = Obstacle()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, obstacle_lower0, obstacle_lower1,
                    obstacle_lower2, obstacle_upper0, obstacle_upper1, obstacle_upper2)
    obstacles = pygame.sprite.Group()
    obstacles.add(obstacle_lower0, obstacle_lower1, obstacle_lower2,
                  obstacle_upper0, obstacle_upper1, obstacle_upper2)

    choices = [4, 5, 6]
    for i in range(3):
        Spawn(obstacles.sprites()[i+3], obstacles.sprites()[i], choices, True)

    # game loop
    while game.run:
        game.Events()
        player.Keys()

        # move
        player.move()
        player.jump()
        player.isJump = False
        for obstacle in obstacles:
            obstacle.move()
        
        
        
        #spawn + score counter
        for i in range(3):
            Spawn(obstacles.sprites()[i+3], obstacles.sprites()[i], choices, False)
            if obstacles.sprites()[i].rect.x == player.rect.x-3:
                player.score.score +=1
                sounds.point.play()
        Spawn_Control(obstacles)
                
        # canvas
        game.display.blit(assets.background, (0, 0))
        all_sprites.draw(game.display)
        game.display.blit(assets.floor, (0, 450))
        player.score.PrintScore(game.display,game.screen)


        #collision + endgame
        if pygame.sprite.spritecollideany(player, obstacles):
            GameEnd(obstacles,player,game,sounds,assets,game.fps,framespersec)

        #fps + screen update
        framespersec.tick(game.fps)
        pygame.display.update()

if __name__ == "__main__":
    main()
