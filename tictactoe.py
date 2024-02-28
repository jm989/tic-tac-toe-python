import random

currentPlayer = "X"
winner = None
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
gameRunning = True

def grid():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#Get user input 
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp < 1 and inp > 9:
        print("Invalid input")
    elif board[inp - 1] != "-":
        print("Position taken, chose another position")
    else:
        board[inp - 1] = currentPlayer

    
def checkRows(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
def checkCols(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[5]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def CheckTie(board):
    global gameRunning
    if "-" not in board:
        grid(board)
        print("Tie!!")
        gameRunning = False
        
def checkForWin():
    if checkCols(board) or checkDiag(board) or checkRows(board):
        print(f"The winner is {winner}")
        
'''def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPLayer() '''
def switchPLayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer == "X"

while gameRunning:
    grid()
    playerInput(board)
    checkForWin()
    CheckTie(board)
    switchPLayer()
    checkForWin()
    CheckTie(board)
    

