from random import choice
import string
import os

board = [[0 for i in range(3)] for j in range(3)]
marker = {0: ' ', 1:'X', 2: 'O'}
player = 1

def printboard():
    for i in range(3):
        print('|---|---|---|')
        print(f'| {marker[board[i][0]]} | {marker[board[i][1]]} | {marker[board[i][2]]} |')
    print('|---|---|---|')

def checkwin():
    running = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                running = 1

    if running:
        for row in range(3):
            if board[row][0]==1 and board[row][1]==1 and board[row][2]==1:
                return 'player1'
            elif board[row][0]==2 and board[row][1]==2 and board[row][2]==2:
                return 'player2'
        for col in range(3):
            if board[0][col]==1 and board[1][col]==1 and board[2][col]==1:
                return 'player1'
            elif board[0][col]==2 and board[1][col]==2 and board[2][col]==2:
                return 'player2'
        if ((board[0][0]==1 and board[1][1]==1 and board[2][2]==1) 
            or (board[2][0]==1 and board[1][1]==1 and board[0][2]==1)):
            return 'player1'
        elif ((board[0][0]==2 and board[1][1]==2 and board[2][2]==2) 
            or (board[2][0]==2 and board[1][1]==2 and board[0][2]==2)):
            return 'player2'
        return 'running'
    else:
        for row in range(3):
            if board[row][0]==1 and board[row][1]==1 and board[row][2]==1:
                return 'player1'
            elif board[row][0]==2 and board[row][1]==2 and board[row][2]==2:
                return 'player2'
        for col in range(3):
            if board[0][col]==1 and board[1][col]==1 and board[2][col]==1:
                return 'player1'
            elif board[0][col]==2 and board[1][col]==2 and board[2][col]==2:
                return 'player2'
        if ((board[0][0]==1 and board[1][1]==1 and board[2][2]==1) 
            or (board[2][0]==1 and board[1][1]==1 and board[0][2]==1)):
            return 'player1'
        elif ((board[0][0]==2 and board[1][1]==2 and board[2][2]==2) 
            or (board[2][0]==2 and board[1][1]==2 and board[0][2]==2)):
            return 'player2'
        return 'draw'

def askinput():
    while True:
        pos = input('Please input row and column in (row, column): ')
        pos = pos.replace('(', '')
        pos = pos.replace(')','')
        pos = pos.replace(' ','')
        pos_list=pos.split(',')
        row = int(pos_list[0])
        column = int(pos_list[1])
        if row > 2 or column > 2:
            print('Out of range')
        elif board[row][column] == 0:
            break 
        else:
            print('Invalid input')    
    return row, column
    
    
def main_tictactoe():
    res = 'running'
    global player
    while res =='running':
        print('******************************************************')
        if player == 1:
            print("It is 1st player's (X) turn ")
            row, col = askinput()
            board[row][col] = 1
            res = checkwin()
            player = 2
        else:
            print("It is 2nd player's (O) turn ")
            row, col = askinput()
            board[row][col] = 2
            res = checkwin()
            player = 1
        
        printboard()
        
        if res == 'player1':
            print('Player1 won!')
        elif res == 'player2':
            print('Player2 won!')
        elif res == 'draw':
            print('It is a draw')
        else:
            continue
            
        
        

if __name__=="__main__":

    printboard()
    main_tictactoe()