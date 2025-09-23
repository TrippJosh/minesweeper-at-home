import random
import time

def printS(text):
    print(text)
    time.sleep(1)

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
        return mineNum

printS("Josh's Minesweeper")
size = int(input("Enter size of board (5-20): "))
playing = True

mineTotal = size * size
results = []
revealed = []
while temp != 0:
    temp -= 1
    results.append(genAlgorithm())

while playing == True:
    counter = size
    while counter != 0:
        #print from results list until counter (aka size) is 0, finish later
        print("filler")
    #show screen

    userInput = input("-> ")
    cmd, arg = userInput.split()
    col = ord(arg[0].lower()) - ord('a')
    row = int(arg[1:]) - 1