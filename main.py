import random
import time

def printS(text):
    print(text)
    time.sleep(1)

def genAlgorithm():
    """generates, randomly, whether or not a mine is at a space"""
    try:
        temp = random.randint(1, 100)
        if temp < 61:
            mineNum = 1
        else:
            mineNum = 0

    except:
        print("Error in world generation algorithm!")
    
    finally:
        return mineNum
    
def flag(row, col):
    """handles flagging"""
    print(f"Flagging at {row}, {col}")
    revealed[row][col] = 'F'

def click (row, col):
    """handles clicking and searches surrounding mines (3x3 grid)"""
    print(f"Clicking at {row}, {col}")
    if grid[row][col] == 1:
        print("You hit a mine! Game over.")
        global playing
        playing = False
    else:
        ticking = 8
        displayNum = 0
        tempRow = row
        tempCol = col
        while ticking != 0:
            if tempRow > 0 and tempCol > 0 and grid[tempRow - 1][tempCol - 1] == 1:
                displayNum += 1
            else:
                revealed[tempRow - 1][tempCol - 1] = 0
            if tempRow > 0 and grid[tempRow - 1][tempCol] == 1:
                displayNum += 1
            else:
                revealed[tempRow - 1][tempCol] = 0
            if tempRow > 0 and tempCol < size - 1 and grid[tempRow - 1][tempCol + 1] == 1:
                displayNum += 1
            else:
                revealed[tempRow - 1][tempCol + 1] = 0
            if tempCol > 0 and grid[tempRow][tempCol - 1] == 1:
                displayNum += 1
            else:
                revealed[tempRow][tempCol - 1] = 0
            if tempCol < size - 1 and grid[tempRow][tempCol + 1] == 1:
                displayNum += 1
            else:
                revealed[tempRow][tempCol + 1] = 0
            if tempRow < size - 1 and tempCol > 0 and grid[tempRow + 1][tempCol - 1] == 1:
                displayNum += 1
            else:
                revealed[tempRow + 1][tempCol - 1] = 0
            if tempRow < size - 1 and grid[tempRow + 1][tempCol] == 1:
                displayNum += 1
            else:
                revealed[tempRow + 1][tempCol] = 0
            if tempRow < size - 1 and tempCol < size - 1 and grid[tempRow + 1][tempCol + 1] == 1:
                displayNum += 1
            else:
                revealed[tempRow + 1][tempCol + 1] = 0
            ticking -= 1

        if ticking == 0:
            revealed[row][col] = displayNum

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

if debug == True:
    print("DEBUG MODE ENABLED")
    print("Mine grid:")
    for row in grid:
        print(' '.join(str(cell) for cell in row))

while playing == True:
    print("Current Board:")
    for row in revealed:
        print(' '.join(str(cell) for cell in row))

    userInput = input("-> ")
    cmd, arg = userInput.split()
    col = ord(arg[0].lower()) - ord('a')
    row = int(arg[1:]) - 1

    if cmd == "flag":
        flag(row, col)
    elif cmd == "click":
        click(row, col)
    else:
        print("Unknown command")