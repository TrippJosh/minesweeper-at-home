import random
import time
import sys

blue = "\033[34m"
reset = "\033[0m"
gold = "\033[38;5;220m"

COLORS = {
    '1': "\033[34m",  # Blue
    '2': "\033[32m",  # Green
    '3': "\033[31m",  # Red
    '4': "\033[35m",  # Purple
    '5': "\033[91m",  # Bright Red/Crimson
    '6': "\033[36m",  # Cyan
    '7': "\033[30m",  # Black
    '8': "\033[37m",  # Grey
}
RESET = "\033[0m"

def readScores():
    """
    Reads and returns the contents of the scores.txt file.
    """
    try:
        with open("scores.txt", "r") as file:
            lines = []
            reading = True
            while reading == True:
                tempLine = file.readline()
                if tempLine == "":
                    reading = False
                    break
                else:
                    lines.append(tempLine)
            
            linesSorted = sorted(lines, reverse=True)[:5]

            ##debug print(lines)
            for i in linesSorted:
                print(i.strip())
            print("")
            
    except FileNotFoundError:
        return "No scores available."

def writeScores(name, score):
    """
    Appends the given text to the scores.txt file.
    """
    try:
        compound = str("\n" + str(score) + " " + name)
        with open("scores.txt", "a") as file:
            file.write(compound)
            file.write("\n")
    except Exception as e:
        if debug == True:
            print(f"Error writing to scores file: {e}")
    finally:
        file.close()

def printS(text):
    """
    Prints the given text and pauses for half a second for dramatic effect.
    """
    print(text)
    time.sleep(0.5)

def color_cell(cell):
    """
    Returns the cell value as a colored string if it is a number (1-8), otherwise returns the cell as a string.
    Used for colored Minesweeper board display.
    """
    cell_str = str(cell)
    if cell_str in COLORS:
        return f"{COLORS[cell_str]}{cell_str}{RESET}"
    return cell_str

def genAlgorithm():
    """
    Randomly determines if a mine is placed at a grid location.
    Returns 1 for mine, 0 for empty.
    """
    try:
        temp = random.randint(1, 100)
        if temp < 34:
            mineNum = 1
        else:
            mineNum = 0

    except ValueError:
        if debug == True:
            print("ValueError in world generation algorithm!")
    except TypeError:
        if debug == True:
            print("TypeError in world generation algorithm!")
    except Exception:
        if debug == True:
            print("Unknown error in world generation algorithm!")
    
    finally:
        return mineNum
    
def flag(row, col):
    """
    Flags or unflags a tile at the given row and column.
    Flags if unrevealed, unflags if already flagged, prevents flagging revealed tiles.
    """
    try:
            if revealed[row][col] == 'F':
                print(f"Unflagging at {row}, {col}")
                revealed[row][col] = "."
            elif revealed[row][col] == ".":
                print(f"Flagging at {row}, {col}")
                revealed[row][col] = 'F'
            else:
                print("Cannot flag a revealed tile.")
    except IndexError:
        if debug == True:
            print("IndexError: Invalid flag coordinates.")
    except Exception:
        if debug == True:
            print("Unknown error processing flag command.")

first_click = True

def click(row, col):
    """
    Handles clicking on a tile at the given row and column.
    Reveals the tile, counts nearby mines, and reveals adjacent tiles on first click.
    Prevents clicking flagged tiles and handles game over logic.
    """
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
        print("")
    except IndexError:
        if debug == True:
            print("IndexError: Invalid click coordinates.")
    except ValueError:
        if debug == True:
            print("ValueError: Invalid value during click.")
    except Exception:
        if debug == True:
            print("Unknown error processing click command.")

#################################################################################################startup/intro sequence
print(f"{reset}---{reset}")
printS(f"{blue}Josh's Minesweeper{blue}")
printS("By Josh (github.com/joshua-goulding)")

printS("\n Current High Scores (top 5):")
printS(readScores())

asking = True
while asking == True:
    try:
        size = int(input("Enter size of board (Min. 5): "))
        if 5 > size:
            print("Size too small, there will be a map generation error.")
        else:
            asking = False
    except ValueError:
        print("Please enter a valid integer for the board size.")

print("Pro tip: to see commands, type 'help'.")

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
foundEmpty = 3
while foundEmpty != 0: # finds an empty space to start the game, thrice
    try:
        if grid[startRow][startCol] == 0:
            click(startRow, startCol)
            foundEmpty -= 1
        temp = random.randint(1, 2)
        if temp == 1:
            startRow += 1
        else:
            startCol += 1
    except IndexError:
        print("IndexError: Error finding starting position.")
        break
    except Exception:
        print("Unknown error finding starting position.")
        break

##legend
print(f"{reset}Legend: F = Flagged, . = Unrevealed, Numbers = mines nearby{reset}")

while playing == True:
    try:
        if all(revealed[r][c] != "." and revealed[r][c] != 'F' for r in range(size) for c in range(size) if grid[r][c] == 0):
            print(f"{gold}---{gold}")
            printS("      ___________      ")
            printS("     '._==_==_=_.'     ")
            printS("     .-\\:      /-.    ")
            printS("    | (|:.     |) |    ")
            printS("     '-|:.     |-'     ")
            printS("       \\::.    /      ")
            printS("        '::. .'        ")
            printS("          ) (          ")
            print(f"{gold}Congratulations! You've cleared the board!{gold}")
            scoreName = input("Enter your name for the high score list: ")

            writeScores(scoreName, size)

            question = input("Would you like to play again? (y/n): ").lower()
            print(f"{reset}---{reset}")
            if question == 'y':
                import os
                os.execv(sys.executable, ['python'] + sys.argv)
            else:
                break
        print("Current Board:")
        topper = [str(i+1) for i in range(size)]
        print("   " + " ".join(topper))

        for idx, row in enumerate(revealed):
            print(f"{str(idx+1).rjust(2)} " + ' '.join(color_cell(cell) for cell in row))

        userInput = input("-> ")
        noCoordCmds = ["help", "exit", "debug", "debugShow", "debugStop"]
        for command in noCoordCmds:
            if command == userInput:
                userInput = userInput + " 00"  # padding for no-coordinate commands
        cmd, arg = userInput.split()
        row = int(arg[1]) - 1
        col = int(arg[0]) - 1

        if cmd == "flag":
            flag(row, col)
        elif cmd == "click":
            click(row, col)
        elif cmd == "exit":
            print("Exiting game.")
            break
        elif cmd == "help":
            print("Available commands:")
            print("  flag XY   - Place a flag at coordinates XY (e.g., flag 23)")
            print("  click XY  - Click the tile at coordinates XY (e.g., click 25)")
            print("  exit      - Exit the game")
            if debug == True:
                print("  debug     - Enable debug mode (secret command)")
                print("  debugShow - Show the mine grid (debug mode only)")
                print("  debugStop - Disable debug mode")
        elif cmd == "debugShow":
            if debug == True:
                try:
                    print(f"{reset}DEBUG MODE ENABLED{reset}")
                    print("Mine grid:")
                    for row in grid:
                        print(' '.join(str(cell) for cell in row))
                except Exception:
                        print("Error displaying debug information.")
        elif cmd == "debug":
            debug = True
            print("Debug mode enabled.")
        elif cmd == "debugStop":
            if debug == True:
                debug = False
                print("Debug mode disabled.")
            
    except IndexError:
        print("IndexError: Invalid coordinates. Please enter coordinates within the board size.")
    except ValueError:
        print("ValueError: Invalid input. Please enter a valid command and coordinates.")
    except KeyError:
        print("KeyError: Invalid command. Use 'flag' or 'click'.")
    except Exception:
        print("Unknown error occurred while processing command.")
    
############### end of game loop