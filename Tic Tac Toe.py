import random

#printing the game board

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

current_Player = "X"
winner = None
game_Running= True        

def printBoard(board):
    print(board[0],  " |", board[1],  " |", board[2])
    print("------------")
    print(board[3],  " |", board[4],  " |", board[5])
    print("------------")
    print(board[6],  " |", board[7],  " |", board[8])
##printBoard(board)

#Take input
def playerInput(board):
    inp=int(input("Enter number between 1 and 9\n"))
    if inp >=1 or inp <=9 and board[inp-1]=='-':
        board[inp-1]=current_Player

    else:
        print("Poisition Already Marked!")   
        switchPlayer() 


#Check for win/tie/lose
def checkHorizontal(board):
    global winner
    if   board[0] == board[1] == board[2] and board[0] != '-':
        winner=board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':    
        winner=board[3]
        return True
    
    elif board[6] == board[7] == board[8] and board[6] != '-':    
        winner=board[6]
        return True    

def checkVertical(board):
    global winner
    if   board[0] == board[3] == board[6] and board[0] != '-':
        winner=board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':    
        winner=board[1]
        return True
    
    elif board[2] == board[5] == board[8] and board[2] != '-':    
        winner=board[2]
        return True

def checkDiagonal(board):
    global winner
    if   board[0] == board[4] == board[8] and board[0] != '-':
        winner=board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':    
        winner=board[2]
        return True
 
def checkTie(board):
    global game_Running
    if "-" not in board:
        printBoard(board)
        print("Game draw!")
        game_Running=False           

def checkWin():
    if checkHorizontal(board) or checkVertical(board) or checkVertical(board):
        print("The winner is ", winner)
        printBoard(board)
        global game_Running
        game_Running = False


#Switch player
def switchPlayer():
    global current_Player
    if current_Player == "X":
        current_Player = "O"
    else:
        current_Player="X"    


#Set Computer to play (Comment this for mutiplayer)
def computer(board):
    if current_Player == "O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchPlayer()


#Check for win/tie/lose

while game_Running:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)

