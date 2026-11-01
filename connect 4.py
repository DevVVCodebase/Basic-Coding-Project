import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if(gameBoard[x][y] == "🔵"):
                print("",gameBoard[x][y], end=" |")
            elif(gameBoard[x][y] == "🔴"):
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def check_win(turn):
    # Horizontal
    for r in range(rows):
        for c in range(cols-3):
            if all(gameBoard[r][c+i] == turn for i in range(4)):
                return True
    # Vertical
    for c in range(cols):
        for r in range(rows-3):
            if all(gameBoard[r+i][c] == turn for i in range(4)):
                return True
    # Diagonal /
    for r in range(3, rows):
        for c in range(cols-3):
            if all(gameBoard[r-i][c+i] == turn for i in range(4)):
                return True
    # Diagonal \
    for r in range(rows-3):
        for c in range(cols-3):
            if all(gameBoard[r+i][c+i] == turn for i in range(4)):
                return True
    return False

def board_full():
    return all(gameBoard[0][c] != "" for c in range(cols))

turnCounter = 0
while True:
    printGameBoard()
    if turnCounter % 2 == 0:
        print("🔵's turn")
        turn = "🔵"
    else:
        print("🔴's turn")
        turn = "🔴"
    
    spacePicked = input("Pick a column (A-G): ").upper()
    
    if spacePicked not in possibleLetters:
        print("Invalid column. Please choose from A to G.")
        continue
    
    colIndex = possibleLetters.index(spacePicked)
    
    # Find the lowest empty row in the selected column
    for row in range(rows - 1, -1, -1):
        if gameBoard[row][colIndex] == "":
            modifyTurn((row, colIndex), turn)
            break
    else:
        print("Column is full. Please choose another column.")
        continue
    
    if check_win(turn):
        printGameBoard()
        print(f"{turn} wins! Game over.")
        break

    if board_full():
        printGameBoard()
        print("It's a tie! Game over.")
        break

    turnCounter += 1