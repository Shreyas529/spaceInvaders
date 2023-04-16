import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu")

BG = pygame.image.load("background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)



        
    
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))
       

        PLAY_EASY = Button(image=None,pos=(400,200),text_input="EASY",font=get_font(65),base_color="Black",hovering_color="Green")
        PLAY_EASY.changeColor(PLAY_MOUSE_POS)
        PLAY_EASY.update(SCREEN)
        PLAY_MEDIUM = Button(image=None,pos=(400,300),text_input="MEDIUM",font=get_font(65),base_color="Black",hovering_color="Green")
        PLAY_MEDIUM.changeColor(PLAY_MOUSE_POS)
        PLAY_MEDIUM.update(SCREEN)
        PLAY_HARD = Button(image=None,pos=(400,400),text_input="HARD",font=get_font(65),base_color="Black",hovering_color="Green")
        PLAY_HARD.changeColor(PLAY_MOUSE_POS)
        PLAY_HARD.update(SCREEN)




        
        PLAY_BACK = Button(image=None, pos=(400, 500), 
                            text_input="BACK", font=get_font(65), base_color="Black", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_EASY.checkForInput(PLAY_MOUSE_POS):
                    return "EASY"
                elif PLAY_MEDIUM.checkForInput(PLAY_MOUSE_POS):
                    return "MEDIUM"
                elif PLAY_HARD.checkForInput(PLAY_MOUSE_POS):
                    return "HARD"
               
                else:
                    #main_menu()
                    return "NONE"

        pygame.display.update()

def main_menu():
    value="NONE"
    while value=="NONE":
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(400, 250), 
                            text_input="PLAY", font=get_font(50), base_color="#bf0296", hovering_color="White")
        RANKING_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(400, 400), 
                            text_input="RANKING", font=get_font(50), base_color="#bf0296", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(400, 550), 
                            text_input="QUIT", font=get_font(50), base_color="#bf0296", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON,RANKING_BUTTON,QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    value= play()                    
                    if value!="NONE":
                        return value
                        break
                if RANKING_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return "Ranking"               
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        if value!="NONE":
            return value
            # break

        pygame.display.update()
    print("exited while in menu")
    print(value)
    return value
