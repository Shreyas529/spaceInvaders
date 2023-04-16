import pygame
import sys
pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
FONT=pygame.font.Font(None,30)
WINDOW_SIZE=(400,400)
WINDOW_TITLE="Leaderboard"
screen=pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)
scores=[]
with open("Leader Board.txt","r") as file:
    for line in file:
        scores.append(line.strip())
scores.sort(reverse=True)        
y=50
for i,score in enumerate(scores[:10]):
    Leader_text=FONT.render(f"{i+1}.{Leader}",True,WHITE)
    screen.blit(Leader_text,(50,y))
    y+=30
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()            
                
