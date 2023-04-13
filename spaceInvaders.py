import pygame
import random
import math as m

pygame.init()

#width , height
screen = pygame.display.set_mode((800, 600))

running = True

#icons and spaceship
icon=pygame.image.load('spaceship.png')

background=pygame.image.load('5532919.jpg')

#player
playerImg=pygame.image.load('spaceship (1).png')
playerX=370
playerY=480
pxchange=0
pychange=0

#enemy
enemyImg=pygame.image.load('ufo.png')
enemyX=random.randint(0,800)
enemyY=random.randint(50,250)
exchange=0.25
eychange=40

#bullet
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bxchange=0
bychange=0.5
bstate='ready'  #ready = cant seee bullet on screen     fire = can be seen

def player(x,y):
    #draw the img on the screen
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    #draw the img on the screen
    screen.blit(enemyImg,(x,y))
    
def fire_bullet(x,y):
    global bstate
    bstate='fire'
    screen.blit(bulletImg , (x+16,y+10))    

def isCollision(bulletX ,bulletY , enemyX , enemyY):
    distance=m.sqrt(m.pow(enemyX-bulletX,2)+m.pow(enemyY-bulletY,2))
    if distance<27:
        return True
    return False
    
    
pygame.display.set_icon(icon)

pygame.display.set_caption("Space Invaders")

score=0 

while running:
    
    #R,G,B
    screen.fill((0, 0, 0))
    
    #BG
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

        #if keystroke is pressed check which direction
        if event.type==pygame.KEYDOWN:
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
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                pxchange=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                pychange=0
        
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
    
    enemyX+=exchange
    if enemyX<=0:
        exchange=0.25
        enemyY+=eychange
    elif enemyX>=736:
        exchange=-0.25
        enemyY+=eychange
        
    #bullet movement
    if bulletY<=0:
        bulletY=480
        bstate='ready'
    
    if bstate=='fire':
        fire_bullet(bulletX,bulletY)
        bulletY-=bychange
    
    collision=isCollision(bulletX,bulletY,enemyX,enemyY)
    
    if collision:
        bulletY=480
        bstate='ready'
        score+=1
        enemyX=random.randint(0,800)
        enemyY=random.randint(50,250)
        
    enemy(enemyX,enemyY)
    player(playerX,playerY)
    pygame.display.update()        
    