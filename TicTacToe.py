board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

inputRow = 0
inputCol = 0


def checkWin(symbol):
    
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == symbol:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True

    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True

    if board[2][0] == board[1][1] == board[0][2] == symbol:
        return True
    
    return False


def checkTie():
    for row in range(len(board)):
        if " " in board[row]:
            return False
    return True


def letter_to_number(letter):
    return int(ord(letter) - ord('a') + 1)


def spaceOccupied(row, col):
    if board[row - 1][col - 1] == " ":
        return False
    else:
        return True


def printBoard():
    global board
    
    print("\n")
    print("\u0332".join(" A B C\n " + board[0][0] + "|" + board[0][1] + "|" + board[0][2]))
    print("\u0332".join(" " + board[1][0] + "|" + board[1][1] + "|" + board[1][2] + " "))
                        
    print(" " + board[2][0] + "|" + board[2][1] + "|" + board[2][2])


def updateBoard(row, col, symbol):
    try:
        board[row - 1][col - 1] = symbol

    except:
        print("Unacceptable move.")

                
def getInput(symbol):
    global inputCol, inputRow

    while True:
        tInput = input("\n\nInput your move for " + symbol + ":\n")


        if len(tInput) != 2:
            print("Invalid input: Please enter a two-character move")
            continue

        try:
            inputRow = int(tInput[0])
            inputCol = letter_to_number(tInput[1])
        except ValueError:
            try:
                inputRow = int(tInput[1])
                inputCol = letter_to_number(tInput[0])
            except:
                print("Invalid input: Please enter a valid row number (1-3) and column letter (A-C)")
                continue

        if not (1 <= inputRow <= 3 and 1 <= inputCol <= 3):
            print("Invalid input: Please enter a move within the board boundaries")
            continue

        if spaceOccupied(inputRow, inputCol):
            print("Space Occupied")
            continue

        break

    return inputRow, inputCol


playAgain = True

while True:
    while True:
        getInput("X")
        updateBoard(inputRow, inputCol, "X")
        printBoard()
        
        if checkWin("X") == True:
            print("X won, congratulations!")
            break
        
        if checkTie() == True:
            print("It's a tie!")
            break
        
        getInput("O")
        updateBoard(inputRow, inputCol, "O")
        printBoard()
        
        if checkWin("O") == True:
            print("O won, congratulations!")
            break
        
        if checkTie() == True:
            print("It's a tie!")
            
    playAgain = input("Would you like to play again?\n")
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    
    if playAgain.lower() == "no":
        print(":(")
        break


