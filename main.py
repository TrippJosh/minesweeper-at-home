import random
import time
import sys
import pygame

pygame.init()

res = (720, 720)
white = (210, 210, 210)
grey = (170, 170, 170)
darkGrey = (100, 100, 100)

screen = pygame.display.set_mode(res)
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('quit', True, white)
width = screen.get_width()
height = screen.get_height()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 10 <= event.pos[0] <= 100 and 10 <= event.pos[1] <= 50:
                    pygame.quit()
                    sys.exit()

    screen.fill(grey)
    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,white,[width/2,height/2,140,40])
        
    else:
        pygame.draw.rect(screen,darkGrey,[width/2,height/2,140,40])

    screen.blit(text , (width/2+50,height/2))
    pygame.display.update() 

def genAlgorithm():
    """generates numbers for the amount of nearby mines"""
    try:
        temp = random.randint(1, 100)
        if temp < 11:
            mineNum = 1
        elif temp < 21:
            mineNum = 2
        elif temp < 31:
            mineNum = 3
        elif temp < 41:
            mineNum = 4
        elif temp < 51:
            mineNum = 5
        elif temp < 56:
            mineNum = 6
        elif temp < 61:
            mineNum = 7
        elif temp < 66:
            mineNum = 8
        elif temp == 66:
            mineNum = 9
        else:
            mineNum = 0

    except:
        print("Error in world generation algorithm!")
    
    finally:
        print("World generation complete")