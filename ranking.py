import pygame
import sys
from button import Button

pygame.init()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu")

font=pygame.font.Font('freesansbold.ttf',40)
BG = pygame.image.load("background.png")
def yours():
    BACK_RANKING = Button(image=pygame.image.load("Play Rect.png"), pos=(700, 550), 
                                text_input="BACK", font=get_font(40), base_color="black", hovering_color="green")
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG,(0,0))
        BACK_RANKING.changeColor(PLAY_MOUSE_POS)
        BACK_RANKING.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_RANKING.checkForInput(PLAY_MOUSE_POS):
                    return "BACK"
        
        alldata=[]
        with open('./LBE.txt', 'r') as fp:
            for i in fp:
                #print(fp.readline())
                alldata.append(fp.readline().split(':'))
        if(len(alldata)>=5):        
            alldata.sort(key = lambda l: int(l[1].strip()), reverse=True)
            a=font.render(f"{alldata[0][0]}:{alldata[0][1].strip()}",True,(255,10,105))
            SCREEN.blit(a,(10,100))
            b=font.render(f"{alldata[1][0]}:{alldata[1][1].strip()}",True,(255,10,105))
            SCREEN.blit(b,(10,200))
            c=font.render(f"{alldata[2][0]}:{alldata[2][1].strip()}",True,(255,10,105))
            SCREEN.blit(c,(10,300))
            d=font.render(f"{alldata[3][0]}:{alldata[3][1].strip()}",True,(255,10,105))
            SCREEN.blit(d,(10,400))
            e=font.render(f"{alldata[4][0]}:{alldata[4][1].strip()}",True,(255,10,105))
            SCREEN.blit(e,(10,500))
        else:
            alldata.sort(key = lambda l: int(l[1].strip()), reverse=True)
            for i in range(len(alldata)):
                z=font.render(f"{alldata[i][0]}:{alldata[i][1].strip()}",True,(255,10,105))
                SCREEN.blit(z,(10,100*i+100))
                
        t=font.render("EASY",True,(245,245,220))  
        SCREEN.blit(t,(10,0))

        blldata=[]
        with open('./LBM.txt', 'r') as fp:
            for i in fp:
                #print(fp.readline())
                blldata.append(fp.readline().split(':'))
        blldata.sort(key = lambda l: int(l[1].strip()), reverse=True)
        if(len(blldata)>=5):
            f=font.render(f"{blldata[0][0]}:{blldata[0][1].strip()}",True,(255,10,105))
            SCREEN.blit(f,(300,100))
            g=font.render(f"{blldata[1][0]}:{blldata[1][1].strip()}",True,(255,10,105))
            SCREEN.blit(g,(300,200))
            h=font.render(f"{blldata[2][0]}:{blldata[2][1].strip()}",True,(255,10,105))
            SCREEN.blit(h,(300,300))
            i=font.render(f"{blldata[3][0]}:{blldata[3][1].strip()}",True,(255,10,105))
            SCREEN.blit(i,(300,400))
            j=font.render(f"{blldata[4][0]}:{blldata[4][1].strip()}",True,(255,10,105))
            SCREEN.blit(j,(300,500))
        else:
            for i in range(len(blldata)):
                z=font.render(f"{blldata[i][0]}:{blldata[i][1].strip()}",True,(255,10,105))
                SCREEN.blit(z,(300,100+i*100))
        u=font.render("MEDIUM",True,(245,245,220))  
        SCREEN.blit(u,(300,0))
        
        clldata=[]
        with open('./LBH.txt', 'r') as fp:
            for i in fp:
                #print(fp.readline())
                clldata.append(fp.readline().split(':'))
        clldata.sort(key = lambda l: int(l[1].strip()), reverse=True)
        if(len(clldata)>=5):
            k=font.render(f"{clldata[0][0]}:{clldata[0][1].strip()}",True,(255,10,105))
            SCREEN.blit(k,(600,100))
            l=font.render(f"{clldata[1][0]}:{clldata[1][1].strip()}",True,(255,10,105))
            SCREEN.blit(l,(600,200))
            m=font.render(f"{clldata[2][0]}:{clldata[2][1].strip()}",True,(255,10,105))
            SCREEN.blit(m,600,300)
            n=font.render(f"{clldata[3][0]}:{clldata[3][1].strip()}",True,(255,10,105))
            SCREEN.blit(n,(600,400))
            o=font.render(f"{clldata[4][0]}:{clldata[4][1].strip()}",True,(255,10,105))
            SCREEN.blit(o,(600,500))
        else:
            for i in range(len(clldata)):
                z=font.render(f"{clldata[i][0]}:{clldata[i][1].strip()}",True,(255,10,105))
                SCREEN.blit(z,(600,100+i*100))
        v=font.render("HARD",True,(245,245,220))  
        SCREEN.blit(v,(600,0))

        pygame.display.update()
        