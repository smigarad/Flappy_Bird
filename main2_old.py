import sys, pygame, random, time
from pygame.locals import*


class Game():
    def __init__(self):
        super().__init__()
        self.screen = (285,500)
        self.display = pygame.display.set_mode(self.screen)
        self.run =0

    def Start(self):
        self.run =1
        pygame.init()

    def Quit(self):
        self.run =0
        time.sleep(2)
        pygame.quit()
        sys.exit()

    def Events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                self.Quit()


#background | assets
class Background_Assets():
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("assets/sprites/background-night.png")
        self.floor = pygame.image.load("assets/sprites/base.png")
        pygame.display.set_caption("Flappy bird")
        self.icon = pygame.image.load("assets/favicon.ico")
        pygame.display.set_icon(self.icon)
        self.gameover = pygame.image.load("assets/sprites/gameover.png")

#functions with score
class Score():
    def __init__(self):
        super().__init__()
        self.score =0
    def LoadScore(score:int):
        return pygame.image.load(f"assets/sprites/{score}.png")

    def PrintScore(self,score: int, display : pygame.Surface, screen: list):
        if score >9:
            score_last_digit = score % 10
            score_first_digit = score // 10
        else:
            score_img = self.LoadScore(score)

        if score <10:
            display.blit(score_img,(screen[0] /2 - 10,100))

        elif score <100:
            score_img = self.LoadScore(score_first_digit)
            display.blit(score_img,(screen[0] /2 - 25,100))
            score_img = self.LoadScore(score_last_digit)
            display.blit(score_img,(screen[0] /2 - 5,100))
    
class Sounds():
    def __init__(self):
        super().__init__()
        self.wing = pygame.mixer.Sound("assets/audio/wing.wav")
        self.die = pygame.mixer.Sound("assets/audio/die.wav")
        self.point = pygame.mixer.Sound("assets/audio/point.wav")
        self.hit = pygame.mixer.Sound("assets/audio/hit.wav")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/yellowbird-downflap.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)
        self.isJump = False
        self.jumpCount = 12
        self.score =Score()
        
    def move(self):
        if self.rect.y >=430:
            self.rect.y =430
        elif self.rect.y <0:
            self.rect.y =0
        else:
            self.rect.move_ip(0,4) 
    
    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -12:
                neg =1
            if self.jumpCount < 0:
                neg =1
            self.rect.y -= self.jumpCount **2 * 0.1 * neg
            self.jumpCount -=1
        else:
            self.isJump = False
            self.jumpCount = 12
    
    def fall(self):
        
        self.rect.y += self.rect.y**0.3
        
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/pipe-green.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100,300),random.choice([0,500]))
        self.speed = 2

    def move(self):
        self.rect.move_ip(-self.speed,0)  

    def draw(self,surface):
        surface.blit(self.image,self.rect)


def QuitGame():
        time.sleep(2)
        pygame.quit()
        sys.exit()
def Events():
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def Spawn(OBSTACLE_UPPER: Obstacle,OBSTACLE_LOWER: Obstacle, RANDOM: int):

    if RANDOM == 4:
        random_x = 800
    if RANDOM ==5:
        random_x = 500
    if RANDOM ==6:
        random_x = 300
        
    random_y =random.randint(0,150)
    OBSTACLE_UPPER.rect.center= (random_x,400 +random_y)
    OBSTACLE_LOWER.rect.center= (random_x,0 +random_y)


def PrintScore(SCORE: int, SCORES: list, DISPLAY : pygame.Surface):
    if SCORE <10:
        DISPLAY.blit(SCORES[SCORE],(SCREEN[0] /2 - 10,100))
    elif SCORE <100:
        DISPLAY.blit(SCORES[SCORE // 10],(SCREEN[0] /2 - 25,100))
        DISPLAY.blit(SCORES[SCORE % 10],(SCREEN[0] /2 - 5,100))



pygame.init()
#screen 
SCREEN = (285,500) #x y

#Background img, surface, floor
BACKGROUND = pygame.image.load("assets/sprites/background-night.png")
FLOOR = pygame.image.load("assets/sprites/base.png")
DISPLAY = pygame.display.set_mode(SCREEN)
pygame.display.set_caption("Flappy bird")

#ICON
ICON = pygame.image.load("assets/favicon.ico")
pygame.display.set_icon(ICON)

#Gameover
GAMEOVER = pygame.image.load("assets/sprites/gameover.png")

#Audio

WING_SOUND = pygame.mixer.Sound("assets/audio/wing.wav")
DIE_SOUND = pygame.mixer.Sound("assets/audio/die.wav")
POINT_SOUND = pygame.mixer.Sound("assets/audio/point.wav")
HIT_SOUND = pygame.mixer.Sound("assets/audio/hit.wav")
#FPS
FPS =30
FramesPerSec = pygame.time.Clock()

#Score -- předělat do funkce :) 
SCORE = 0 
SCORE_00 = pygame.image.load("assets/sprites/0.png")
SCORE_01 = pygame.image.load("assets/sprites/1.png")
SCORE_02 = pygame.image.load("assets/sprites/2.png")
SCORE_03 = pygame.image.load("assets/sprites/3.png")
SCORE_04 = pygame.image.load("assets/sprites/4.png")
SCORE_05 = pygame.image.load("assets/sprites/5.png")
SCORE_06 = pygame.image.load("assets/sprites/6.png")
SCORE_07 = pygame.image.load("assets/sprites/7.png")
SCORE_08 = pygame.image.load("assets/sprites/8.png")
SCORE_09 = pygame.image.load("assets/sprites/9.png")
SCORES = [SCORE_00,SCORE_01,SCORE_02,SCORE_03,SCORE_04,SCORE_05,SCORE_06,SCORE_07,SCORE_08,SCORE_09]


#Player + obstacles group
P1 = Player()
O1 = Obstacle() #LOWER
O2 = Obstacle()
O3 = Obstacle()
O4 = Obstacle() #UPPPER
O5 = Obstacle()
O6 = Obstacle()

OBSTACLES = pygame.sprite.Group() #all obstacles
OBSTACLES.add(O1)
OBSTACLES.add(O2)
OBSTACLES.add(O3)
OBSTACLES.add(O4)
OBSTACLES.add(O5)
OBSTACLES.add(O6)

LOWER_OBSTACLES = pygame.sprite.Group() #lower side
LOWER_OBSTACLES.add(O1)
LOWER_OBSTACLES.add(O2)
LOWER_OBSTACLES.add(O3)

UPPER_OBSTACLES = pygame.sprite.Group() #upper side
UPPER_OBSTACLES.add(O4)
UPPER_OBSTACLES.add(O5)
UPPER_OBSTACLES.add(O6)


for entity in UPPER_OBSTACLES:
    entity.image = pygame.image.load("assets/sprites/pipe-green-down.png")
    

choices = [4,5,6]

choice = choices.pop()
choices.insert(0,choice)   
Spawn(O1,O4,choice)
choice = choices.pop()
choices.insert(0,choice)
Spawn(O2,O5,choice)
choice = choices.pop()
choices.insert(0,choice)
Spawn(O3,O6,choice)

ALL_SPRITES = pygame.sprite.Group()
ALL_SPRITES.add(OBSTACLES)
ALL_SPRITES.add(P1)
jump_count =0
SCORE = 8

#rot

ROT = 0
ROT_SPEED = 2



#game loop
while True:
    print (jump_count)
    Events() #eventy - vypínání
    KEYS = pygame.key.get_pressed()
    if KEYS[K_q]:
        time.sleep(1)
        pygame.quit()
        sys.exit()
    if KEYS[K_SPACE]:                   #retarded jump system 
        if jump_count >17:
            P1.isJump= False
            jump_count+=1
        else:
            P1.isJump= True
            jump_count+=1

    if P1.isJump == False:
        jump_count =0
    
#jumping and moving
    P1.jump()
    P1.move()

    for entity in OBSTACLES:
        entity.move()   
            
    for entity in LOWER_OBSTACLES:
        if entity.rect.x == P1.rect.x -3:
            SCORE +=1
            POINT_SOUND.play()

    if O1.rect.x <= -70:
        choice = choices.pop()
        choices.insert(0,choice)
        Spawn(O1,O4,choice)
    if O2.rect.x <= -70:
        choice = choices.pop()
        choices.insert(0,choice)
        Spawn(O2,O5,choice)
    if O3.rect.x <= -70:
        choice = choices.pop()
        choices.insert(0,choice)
        Spawn(O3,O6,choice)

    P1.isJump= False
    
    #collision
    #end game
    if pygame.sprite.spritecollideany(P1,OBSTACLES):
        HIT_SOUND.play()
        time.sleep(0.5)
        DIE_SOUND.play()
        while P1.rect.y <=SCREEN[1] +20:
            if ROT <88:
                ROT = ( ROT +ROT_SPEED) %90 
            print(ROT)
            surface = pygame.transform.rotate(P1.image,-ROT)
            P1.fall()
            
            DISPLAY.blit(BACKGROUND, (0,0))
            #ALL_SPRITES.draw(DISPLAY)
            OBSTACLES.draw(DISPLAY)
            DISPLAY.blit(surface,P1.rect)
            PrintScore(SCORE,SCORES,DISPLAY)
            DISPLAY.blit(GAMEOVER, (40,200))
            DISPLAY.blit(FLOOR, (0,450))
            pygame.display.update()
            FramesPerSec.tick(FPS)
        DISPLAY.blit(GAMEOVER, (40,200))

        pygame.display.update()
        for entity in ALL_SPRITES:
            entity.kill()
        QuitGame()
    
 #drawing on canvas       
    DISPLAY.blit(BACKGROUND, (0,0))
    
    ALL_SPRITES.draw(DISPLAY)
    DISPLAY.blit(FLOOR, (0,450))
    PrintScore(SCORE,SCORES,DISPLAY)


    pygame.display.update()
    FramesPerSec.tick(FPS)


    