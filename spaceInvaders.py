import pygame
import random
import math as m
import threading

pygame.init()

#width , height
screen = pygame.display.set_mode((800, 600))

running = True

#icons and spaceship
icon=pygame.image.load('spaceship.png').convert_alpha()

background=pygame.image.load('background.jpg').convert_alpha()

#player
playerImg=pygame.image.load('spaceship (1).png').convert_alpha()
player_mask=pygame.mask.from_surface(playerImg)
playerX=370
playerY=480
pxchange=0
pychange=0

#enemy

enemyImg=[]
enemy_mask=[]
enemyY=[]
enemyX=[]
exchange=[]
eychange=[]
noe=6

for i in range(noe):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemy_mask.append(pygame.mask.from_surface(enemyImg[i]))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,250))
    exchange.append(1) 
    eychange.append(40)

#bullet
bulletImg=pygame.image.load('bullet.png').convert_alpha()
bullet_mask=pygame.mask.from_surface(bulletImg)
bulletX=0
bulletY=playerY
bxchange=0
bychange=0.75
bstate='ready'  #ready = cant seee bullet on screen     fire = can be seen


def player(x,y):
    #draw the img on the screen
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    #draw the img on the screen
    screen.blit(enemyImg[i],(x,y))
    
def fire_bullet(x,y):
    global bstate
    bstate='fire'
    screen.blit(bulletImg , (x+16,y+10))    

def isCollision(bulletX ,bulletY , enemyX , enemyY):
    distance=m.sqrt(m.pow(enemyX-bulletX,2)+m.pow(enemyY-bulletY,2))
    if distance<27 and bstate=='fire':
        return True
    return False
    
    
pygame.display.set_icon(icon)

pygame.display.set_caption("Space Invaders")

#score
score_value=0
font = pygame.font.Font('freesansbold.ttf',32)

textX=10
testY=10

def show_score(x,y):
    score=font.render("Score :"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

over_font=pygame.font.Font('freesansbold.ttf',64)

def display_over():
    over_text=over_font.render("GAME OVER",True,(0,0,0))
    reset_text=font.render("Press Space to restart",True,(0,0,0))
    screen.blit(reset_text,(230 , 350))
    global score_value
    score_value=0
    screen.blit(over_text,(200,250))
    pygame.display.update()  

game_active=True

def place_enemy():
    for i in range(noe):
        enemyX[i]=(random.randint(0,735))
        enemyY[i]=(random.randint(50,250))

FONT = pygame.font.SysFont("Roboto", 100)

# Clock
CLOCK = pygame.time.Clock()

# Work
WORK = 50000000

# Loading BG
LOADING_BG = pygame.image.load("Loading Bar Background.png")
LOADING_BG_RECT = LOADING_BG.get_rect(center=(400, 300))

# Loading Bar and variables
loading_bar = pygame.image.load("Loading Bar.png")
loading_bar_rect = loading_bar.get_rect(midleft=(40, 300))
loading_finished = False
loading_progress = 0
loading_bar_width = 8

def doWork():
	# Do some math WORK amount times
	global loading_finished, loading_progress

	for i in range(WORK):
		math_equation = 523687 / 789456 * 89456
		loading_progress = i 

	loading_finished = True

# Finished text
finished = FONT.render("Done!", True, "white")
finished_rect = finished.get_rect(center=(400, 300))

# Thread
threading.Thread(target=doWork).start()


while running:
    
    #R,G,B
    screen.fill((0, 0, 0))
    
    #BG
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

        #if keystroke is pressed check which direction
        if event.type==pygame.KEYDOWN and game_active:
            if event.key==pygame.K_LEFT:
                pxchange=-0.35
            if event.key==pygame.K_RIGHT:
                pxchange= 0.35
            if event.key==pygame.K_UP:
                pychange=-0.35 
            if event.key==pygame.K_DOWN:
                pychange=0.35  
            if event.key==pygame.K_SPACE and bstate=='ready':
                bulletX=playerX
                fire_bullet(bulletX,bulletY)
                
        if event.type==pygame.KEYUP and game_active:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                pxchange=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                pychange=0
                
    
    if loading_finished:
        if game_active:    
            playerX+=pxchange
            playerY+=pychange
            if playerX>800:
                playerX=0
            if playerX<0:
                playerX=800
            if playerY<0:
                playerY=600
            if playerY>600:
                playerY=0
            
            for i in range(noe):
                enemyX[i]+=exchange[i]
                if enemyX[i]<=0:
                    exchange[i]=1
                    enemyY[i]+=eychange[i]
                elif enemyX[i]>=736:
                    exchange[i]=-1
                    enemyY[i]+=eychange[i]
                    
                collision=isCollision(bulletX,bulletY,enemyX[i],enemyY[i])
            
                if collision:
                    bulletY=playerY
                    bstate='ready'
                    score_value+=1
                    enemyX[i]=random.randint(0,735)
                    enemyY[i]=random.randint(50,250)
                
                enemy(enemyX[i],enemyY[i],i)
                
                game_active=not player_mask.overlap(enemy_mask[i],(enemyX[i]-playerX,enemyY[i]-playerY))
                if game_active==False:
                    break

            if bulletY<=0:
                bulletY=playerY
                bstate='ready'
            
            if bstate=='fire':
                fire_bullet(bulletX,bulletY)
                bulletY-=bychange
                
            show_score(textX,testY)
            player(playerX,playerY)
            
        else:
            screen.fill((255,255,255))
            display_over()
            pygame.display.update()
            run = True
            game_active=True
            
            while(run):
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                    if (event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
                        score_value=0
                        run = False
            place_enemy()
            playerX=370
            playerY=480
            pxchange,pychange=0,0
            player(playerX,playerY)
                    
    else:
        loading_bar_width = loading_progress / WORK * 725
        loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
        loading_bar_rect = loading_bar.get_rect(midleft=(40, 300))
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        screen.blit(loading_bar, loading_bar_rect)
  
  
    pygame.display.update()