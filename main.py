import random
import time
import sys

def printS(text):
    print(text)
    time.sleep(1)

def genAlgorithm():
    """generates, randomly, whether or not a mine is at a space"""
    try:
        temp = random.randint(1, 100)
        if temp < 34:
            mineNum = 1
        else:
            mineNum = 0

    except:
        print("Error in world generation algorithm!")
    
    finally:
        return mineNum
    
def flag(row, col):
    """handles flagging"""
    try:
        print(f"Flagging at {col+1}, {row+1}")
        revealed[row][col] = 'F'
    except:
        print("Error processing flag command.")

first_click = True

def click(row, col):
    """handles clicking process"""
    try:
        global first_click, playing
        print(f"Clicking at {col+1}, {row+1}")
        if revealed[row][col] == 'F':
            print(f"Tile at {row+1}, {col+1} is flagged. Cannot click a flagged tile.")
            return
        if grid[row][col] == 1:
            print("You hit a mine! Game over.")
            question = input("Would you like to play again? (y/n): ").lower()
            if question == 'y':
                import os
                os.execv(sys.executable, ['python'] + sys.argv)
            else:
                playing = False
        else:
            # Count nearby mines
            displayNum = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < size and 0 <= nc < size:
                        if grid[nr][nc] == 1:
                            displayNum += 1

            revealed[row][col] = displayNum

            if first_click:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < size and 0 <= nc < size:
                            if grid[nr][nc] == 0 and revealed[nr][nc] == ".":
                                neighbor_mines = 0
                                for dr2 in [-1, 0, 1]:
                                    for dc2 in [-1, 0, 1]:
                                        if dr2 == 0 and dc2 == 0:
                                            continue
                                        nnr, nnc = nr + dr2, nc + dc2
                                        if 0 <= nnr < size and 0 <= nnc < size:
                                            if grid[nnr][nnc] == 1:
                                                neighbor_mines += 1
                                revealed[nr][nc] = neighbor_mines
                first_click = False
    except:
        print("Error processing click command.")

#startup/intro sequence
printS("Josh's Minesweeper")
size = int(input("Enter size of board (5-20): "))
debugQ = input("Enable debug mode? (y/n): ").lower()
print("Pro tip: the only commands are 'flag' and 'click', followed by the coordinates (e.g. 'flag 23' or 'click 25')")
if debugQ == 'y':
    debug = True
else:
    debug = False
playing = True

mineTotal = size * size
rowCounter = 0
columnCounter = 0
grid = [[0 for _ in range(size)] for _ in range(size)]
revealed = [[False for _ in range(size)] for _ in range(size)]

while mineTotal != 0: # fills the grid with mines
    while columnCounter != size:
        grid[rowCounter][columnCounter] = genAlgorithm()
        columnCounter += 1
        mineTotal -= 1
    
    if columnCounter == size:
        columnCounter = 0
        rowCounter += 1

mineTotal = size * size
rowCounter = 0
columnCounter = 0

while mineTotal != 0: # fills the revealed grid with .
    while columnCounter != size:
        revealed[rowCounter][columnCounter] = "."
        columnCounter += 1
        mineTotal -= 1
    
    if columnCounter == size:
        columnCounter = 0
        rowCounter += 1

startRow = 1
startCol = 1
foundEmpty = False
while foundEmpty == False: # finds an empty space to start the game
    try:
        if grid[startRow][startCol] == 0:
            click(startRow, startCol)
            foundEmpty = True
        else:
            startRow += 1
            startCol += 1
    except:
        print("Error finding starting position.")

if debug == True:
    try:
        print("DEBUG MODE ENABLED")
        print("Mine grid:")
        for row in grid:
            print(' '.join(str(cell) for cell in row))
    except:
        print("Error displaying debug information.")

##legend
print("Legend: F = Flagged, . = Unrevealed, Numbers = ")

while playing == True:
    try:
        print("Current Board:")

        for row in revealed:
            print(' '.join(str(cell) for cell in row))

        userInput = input("-> ")
        cmd, arg = userInput.split()
        row = int(arg[1]) - 1
        col = int(arg[0]) - 1

        if cmd == "flag":
            flag(row, col)
        elif cmd == "click":
            click(row, col)
    except:
        print("Unknown command")
    
