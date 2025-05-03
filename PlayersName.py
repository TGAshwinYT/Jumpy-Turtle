import pygame,sys,button
import Jumpy_Main
from Scoreboard import *

def log():
    pygame.init()
    clock = pygame.time.Clock()
    f=open(r"assets/text file/PlayerName_Login.txt","w")

    #create display window
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 400

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Log_In')
    base_font = pygame.font.Font(None,40)
    Players_Name= ''

    #Load button images
    start_img = pygame.image.load(r'assets/images/start_btn.png').convert_alpha()
    name_img = pygame.image.load(r'assets/images/name_btn.png').convert_alpha()
        
    #create button instances
    start_button = button.Button(113, 350, start_img, 0.7)
    name_button = button.Button(125, 85, name_img, 0.6)

    #Text 
    input_rect = pygame.Rect(159,220,140,40)
    color_active = pygame.Color('white')
    color_passive = pygame.Color('gray15')
    color = color_passive

    active = False

    #game loop
    run = True
    while run:

        screen.fill((202, 228, 241))

        pygame.draw.rect(screen,color,input_rect,2)

        text_surface = base_font.render(Players_Name,True,(255,255,255))
        screen.blit(text_surface,(input_rect.x + 5,input_rect.y + 5))

        input_rect.w = max(100,text_surface.get_width()+10)

        if start_button.draw(screen):
            f.write(Players_Name)
            print(Players_Name)
            f.flush()
            Score_retive()
            Jumpy_Main.MainGame()
            Save()

        if name_button.draw(screen):
            pass

        #event handler
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        Players_Name = Players_Name[:-1]
                    else:
                        Players_Name+= event.unicode

        if active:
            color = color_active
        else:
            color = color_passive

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
