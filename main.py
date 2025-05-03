import pygame
import button
import PlayersName
from pygame import mixer

mixer.init()
pygame.init()

#create display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Main Menu')

#load button images
start_img = pygame.image.load('assets/images/start_btn.png').convert_alpha()
exit_img = pygame.image.load('assets/images/exit_btn.png').convert_alpha()

#create button instances
start_button = button.Button(99, 150, start_img, 0.8)
exit_button = button.Button(115, 350, exit_img, 0.8)

menu_state = ""

pygame.mixer.music.load('assets/intro.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1, 0.0)

#game loop
run = True
while run:

        screen.fill((202, 228, 241))

        if start_button.draw(screen):
                menu_state = "start"
        if exit_button.draw(screen):
                run = False
        if menu_state == "start":
                PlayersName.log()

        #event handler
        for event in pygame.event.get():
                #quit game
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()

pygame.quit()
