import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)



        
    
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_EASY = Button(image=None,pos=(640,300),text_input="EASY",font=get_font(75),base_color="Black",hovering_color="Green")
        PLAY_EASY.changeColor(PLAY_MOUSE_POS)
        PLAY_EASY.update(SCREEN)
        PLAY_MEDIUM = Button(image=None,pos=(640,400),text_input="MEDIUM",font=get_font(75),base_color="Black",hovering_color="Green")
        PLAY_MEDIUM.changeColor(PLAY_MOUSE_POS)
        PLAY_MEDIUM.update(SCREEN)
        PLAY_HARD = Button(image=None,pos=(640,500),text_input="HARD",font=get_font(75),base_color="Black",hovering_color="Green")
        PLAY_HARD.changeColor(PLAY_MOUSE_POS)
        PLAY_HARD.update(SCREEN)
        
        PLAY_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_EASY.checkForInput(PLAY_MOUSE_POS):
                    return 1
                elif PLAY_MEDIUM.checkForInput(PLAY_MOUSE_POS):
                    return 2
                elif PLAY_HARD.checkForInput(PLAY_MOUSE_POS):
                    return 3
                else:
                    main_menu()

        pygame.display.update()
def leaderboard():
    while True:
        LEADERBOARD_MOUSE_POS=pygame.mouse.get_pos()
        SCREEN.blit(BG,(0,0))
        LEADERBOARD_EASY=Button(image=None,pos=(640,300),text_input="EASY",font=get_font(75),base_color="black",hovering_color="green")
        LEADERBOARD_EASY.changeColor(LEADERBOARD_MOUSE_POS)
        LEADERBOARD_EASY.update(SCREEN)
        LEADERBOARD_MEDIUM=Button(image=None,pos=(640,400),text_input="MEDIUM",font=get_font(75),base_color="black",hovering_color="green")
        LEADERBOARD_MEDIUM.changeColor(LEADERBOARD_MOUSE_POS)
        LEADERBOARD_MEDIUM.update(SCREEN)
        LEADERBOARD_HARD=Button(image=None,pos=(640,500),text_input="HARD",font=get_font(75),base_color="black",hovering_color="green")
        LEADERBOARD_HARD.changeColor(LEADERBOARD_MOUSE_POS)
        LEADERBOARD_HARD.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEADERBOARD_EASY.checkForInput(LEADERBOARD_MOUSE_POS):
                    return 1
                elif LEADERBOARD_MEDIUM.checkForInput(LEADERBOARD_MOUSE_POS):
                    return 2
                elif LEADERBOARD_HARD.checkForInput(LEADERBOARD_MOUSE_POS):
                    return 3
                else:
                    main_menu()

        pygame.display.update()
def main_menu():
    
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#bf0296", hovering_color="White")
        RANKING_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400), 
                            text_input="RANKINGS", font=get_font(75), base_color="#bf0296", hovering_color="White")
        
        
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#bf0296", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON,  QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if RANKING_BUTTON.checkForInput(MENU_MOUSE_POS):
                    leaderboard()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
