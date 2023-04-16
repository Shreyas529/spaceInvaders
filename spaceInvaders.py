import pygame
import random
import math as m
import threading
from menu import *
from button import Button
from username import *
from pygame import mixer
from ranking import *

mixer.music.load('Poly.mp3')
mixer.music.play(10)
choice = main_menu()

while(True):
 
 if(choice=="EASY"):
     exspeed=0.35
     eyspeed=35
     name=get_user_name()
     break
     

    
 elif(choice=="MEDIUM"):
     exspeed=0.5
     eyspeed=40
     name=get_user_name()
     break
     
    
 elif(choice=="HARD"):
     exspeed=0.75
     eyspeed=50
     name=get_user_name()
     break
 
 else:
     yours()
     choice=main_menu()

original_x_speed=exspeed
original_y_speed=eyspeed
pygame.init()
#width , height
screen = pygame.display.set_mode((800, 600))
mixer.music.load('background.wav')
mixer.music.play(-1)

running = True

#icons and spaceship
icon=pygame.image.load('spaceship.png').convert_alpha()
background=pygame.image.load('background.png').convert_alpha()
exit_button=pygame.image.load('sign-out.png').convert_alpha()
exit_rect=exit_button.get_rect(topright=(800,0))
pause_button=pygame.image.load('pause.png').convert_alpha()
pause_rect=pause_button.get_rect(topright=(700,0))
slow_down=pygame.image.load('slow-down.png').convert_alpha()
slow_rect=slow_down.get_rect()

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
    exchange.append(exspeed) 
    eychange.append(eyspeed)
    
def change_enemy_speed(noe):
    for i in range(noe):
        if(exchange[i]<0):
            exchange[i]-=exspeed
        else:
            eychange[i]+=eyspeed

def slow_enemy_speed():
     for i in range(noe):
         if(exchange[i]<0):
             exchange[i]=-1*original_x_speed
         else:
             eychange[i]=original_x_speed
            

#bullet
bulletImg=pygame.image.load('bullet.png').convert_alpha()
bullet_mask=pygame.mask.from_surface(bulletImg)
bulletX=0
bulletY=playerY
bxchange=0
bychange=0.75
bstate='ready'  #ready = cant see bullet on screen     fire = can be seen

name_list=[]
score_list=[]
score_dict={}

slow_available=False
slow_x=-100
slow_y=-100
last_grabbed=0
speed_sx=0
speed_sy=0.25

def place_orb():
    global slow_x,slow_y,speed_sx,speed_sy,slow_available
    if slow_available:
        slow_x=random.randint(35,765)
        slow_y=random.randint(30,150)
        screen.blit(slow_down,(slow_x,slow_y))
        slow_rect.x=slow_x
        slow_rect.y=slow_y
        slow_available=False
        

def get_list(fp):
    global name_list,score_list,score_dict
    t=[i.split(":") for i in fp.readlines()]
    for i in range(len(t)):
            name_list.append(t[i][0])
            score_list.append(int(t[i][1]))
    
    for j in range(len(score_list)):
        score_dict[score_list[j]]=name_list[j]
        
    sorted(score_list,reverse=True)

def pause(paused):
    global screen,background
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                confirm_exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        
        screen.blit(background,(0,0))
        pause_text=over_font.render("Paused",True,(237, 5, 222))
        resume_text=font.render("Press C to continue",True,(237, 5, 222))
        screen.blit(pause_text,(200,250))
        screen.blit(resume_text,(200,350))
        pygame.display.update()    
        
                        
    
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

score_value=0
previous_score=0

def isCollision(bulletX ,bulletY , enemyX , enemyY):
    distance=m.sqrt(m.pow(enemyX-bulletX,2)+m.pow(enemyY-bulletY,2))
    if distance<32 and bstate=='fire':
        return True
    return False

# file_e=open("LBE.txt","a")
# file_m=open("LBM.txt","a")
# file_h=open("LBH.txt","a")
    
def confirm_exit():
    global background,screen,choice,score_value
    
    while True:
        EXIT_MOUSE_POS=pygame.mouse.get_pos()
        screen.blit(background,(0,0))
        over_text=font.render("Are you sure you want to exit?",True,(237, 5, 222))
        screen.blit(over_text,(50,200))
        EXIT_1=Button(image=None,pos=(340,300),text_input="CONFIRM",font=get_font(32),base_color="Black",hovering_color="Green")
        EXIT_1.changeColor(EXIT_MOUSE_POS)
        EXIT_1.update(screen)
        CANCEL=Button(image=None,pos=(640,300),text_input="CANCEL",font=get_font(32),base_color="Black",hovering_color="Green")
        CANCEL.changeColor(EXIT_MOUSE_POS)
        CANCEL.update(screen)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if EXIT_1.checkForInput(EXIT_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                elif CANCEL.checkForInput(EXIT_MOUSE_POS):
                    return None
        pygame.display.update()
    
    
pygame.display.set_icon(icon)

pygame.display.set_caption("Space Invaders")

#score

font = pygame.font.Font('freesansbold.ttf',32)

textX=10
testY=10

def show_exit():
    screen.blit(exit_button,(735,0))

def show_pause():
    screen.blit(pause_button,(635,0))
    

if  choice=="EASY": file=open("LBE.txt","r")
if  choice=="MEDIUM": file=open("LBM.txt","r")
if  choice=="HARD": file=open("LBH.txt","r")    
get_list(file)

def show_score(x,y):
    global choice
    get_list(file)
    if len(score_list)!=0:  max_score=max(score_list)
    else:   max_score=0
    score=font.render("Score :"+str(score_value),True,(237, 5, 222))
    high_score=font.render("High Score :"+str(max_score),True,(237, 5, 222))
    screen.blit(high_score,(x,y+30))
    screen.blit(score,(x,y))

over_font=pygame.font.Font('freesansbold.ttf',100)


def display_over():
    global score_value,background,choice
    file_e=open("LBE.txt","a")
    file_m=open("LBM.txt","a")
    file_h=open("LBH.txt","a")
    screen.blit(background,(0,0))
    over_text=over_font.render("GAME OVER",True,(237, 5, 222))
    reset_text=font.render("Press Space to restart",True,(237, 5, 222))
    quit_text=font.render("Press Esc to Quit the game",True, (237, 5, 222))
    score=font.render("Score :"+str(score_value),True,(237, 5, 222))
    screen.blit(quit_text,(200,325))
    screen.blit(over_text,(100,200))
    screen.blit(reset_text,(230 , 400))
    screen.blit(score,(320,500))
    if choice=="EASY":  
        file_e.write(name+":"+str(score_value)+"\n")
        file_e.close()
    if choice=="MEDIUM":  
        file_m.write(name+":"+str(score_value)+"\n")
        file_m.close()
    if choice=="HARD":  
        file_h.write(name+":"+str(score_value)+"\n")  
        file_h.close()  
    pygame.display.update()  

game_active=True

def place_enemy():
    for i in range(noe):
        enemyX[i]=(random.randint(0,735))
        enemyY[i]=(random.randint(50,250))
        
def place_specific(i):
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
    global paused
    
    #R,G,B
    screen.fill((0, 0, 0))
    
    #BG
    screen.blit(background,(0,0))
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            confirm_exit()
            break

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
                bullet_Sound=mixer.Sound('laser.wav')
                bullet_Sound.play()
                bulletX=playerX
                fire_bullet(bulletX,bulletY)
                
        if event.type==pygame.KEYUP and game_active:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                pxchange=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                pychange=0
                
        if event.type==pygame.MOUSEBUTTONDOWN:
            left,mid,right=pygame.mouse.get_pressed()
            if left and (not mid) and (not right):
                if exit_rect.collidepoint(event.pos):
                    game_active=False
                    
        if event.type==pygame.MOUSEBUTTONDOWN:
            left,mid,right=pygame.mouse.get_pressed()
            if left and (not mid) and (not right):
                if pause_rect.collidepoint(event.pos):
                    pause(True)

                    
    
    if loading_finished:
        if game_active: 
            show_pause()
            show_exit()
            slow_x+=speed_sx
            slow_y+=speed_sy
            slow_rect.x=slow_x
            slow_rect.y=slow_y
            screen.blit(slow_down,(slow_x,slow_y))
            playerX+=pxchange
            playerY+=pychange
            if playerX>750:
                playerX=0
            if playerX<0:
                playerX=750
            if playerY<100:
                playerY=550
            if playerY>550:
                playerY=100
            
            for i in range(noe):
                enemyX[i]+=exchange[i]
                if enemyX[i]<=0:
                    exchange[i]=0.5
                    enemyY[i]+=eychange[i]
                elif enemyX[i]>=736:
                    exchange[i]=-0.5
                    enemyY[i]+=eychange[i]
                
                if(enemyY[i]>534):  place_specific(i)
                
                collision=isCollision(bulletX,bulletY,enemyX[i],enemyY[i])
            
                if collision:
                    explosion_Sound=mixer.Sound('explosion.wav')
                    explosion_Sound.play()
                    bulletY=playerY
                    bstate='ready'
                    score_value+=1
                    if  score_value%10==0 and score_value != 0:
                        exspeed+=0.15
                        eyspeed+=1.0
                        change_enemy_speed(noe)
                    enemyX[i]=random.randint(0,735)
                    enemyY[i]=random.randint(50,250)
                
                enemy(enemyX[i],enemyY[i],i)
                
                game_active=not player_mask.overlap(enemy_mask[i],(enemyX[i]-playerX,enemyY[i]-playerY))
                if game_active==False:
                    break
            
            if(score_value%15==0 and score_value != 0 and score_value!=previous_score):
                    previous_score=score_value
                    slow_available=True
                    # print("po")
                    place_orb()
            
            orb_collect=isCollision(bulletX,bulletY,slow_x,slow_y)
            if  orb_collect:
                exspeed-=0.25
                eyspeed-=1.5
                change_enemy_speed(noe)               
                bulletY=playerY
                bstate='ready'
                slow_x=-100
                slow_y=-100
            # pygame.display.update()
                
            
            if bulletY<=0:
                bulletY=playerY
                bstate='ready'
            
            if bstate=='fire':
                fire_bullet(bulletX,bulletY)
                bulletY-=bychange
                
            show_score(textX,testY)
            player(playerX,playerY)
            
        else:
            # screen.fill((255,255,255))
            display_over()
            pygame.display.update()
            run = True
            game_active=True
            slow_available=False
            slow_x=-100
            slow_y=-100
            last_grabbed=0
            speed_sx=0
            speed_sy=0.25
            # screen.blit(slow_down,(slow_x,slow_y))
            while(run):
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        confirm_exit()
                        display_over()
                    if (event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
                        score_value=0
                        run = False
                    if (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                        confirm_exit()
                        display_over() 
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
    