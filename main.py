import random
import time
import sys
import pygame

pygame.init()

res = (720,720)
screen = pygame.display.set_mode()
white = (210, 210, 210)
grey = (170, 170, 170)
darkGrey = (100, 100, 100)

width = screen.get_width
height = screen.get_height
smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('quit' ,True, white)

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