import sys
import random

def drawBoard(boardData):
    headerFooter = '\t    1   2   3   4   5   6   7   8'
    border = '\t  +---+---+---+---+---+---+---+---+'

    print(headerFooter)

    for row in range(8):
        print(border)
        dataRow = '\t%s ' %(row + 1)
        for element in range(8):
            if boardData[row][element] != '':
                dataRow += '| ' + boardData[row][element] + ' '
            else:
                dataRow += '|   '
        print(dataRow + '| ' + '%s' %(row + 1))

    print(border)
    print(headerFooter)

def setGame(boardDatas):
    for i in range(8):
        if i == 3:
            boardDatas.append([' ', ' ', ' ', 'X', 'O', ' ', ' ', ' '])
        elif i == 4:
            boardDatas.append([' ', ' ', ' ', 'O', 'X', ' ', ' ', ' '])
        else:
            boardDatas.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

    return boardData

def firstPlayer():
    number = random.randint(0,1)
    if number == 0:
        print('Player first')
        return True
    else:
        print('Computer first')
        return False

def choiceGame():
    while True:
        print()
        players = input('Input your choice X or O : ')

        if players.lower() == 'x':
            print('X','O')
            return 'X','O'
        elif players.lower() == 'o':
            print('O','X')
            return 'O','X'

def choosePosition(continueGames,board):
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        if continueGames:
            enterkey = input('Enter position to play (11 - 88) : ')
        else:
            print('Computer turn: ')
            keys = random.randint(11,89)
            print(keys)
            return keys
        try:
            if enterkey[0] in DIGITS1TO8 and enterkey[1]  in DIGITS1TO8:
                keys = int(enterkey)
                if keys > 10 and keys < 89:
                    if board[int(enterkey[0]) - 1 ][int(enterkey[1]) - 1 ] == ' ':
                        return keys
                    else:
                        print('This position have value')
            else:
                print('This move is not valid')
        except ValueError:
            print('Enter number not string')

def playGame(continueGames,board,columnPositions,rowPositions):

    if continueGames:
        continueGames = False

        boardData[rowPositions][columnPositions] = player
    else:
        continueGames = True
        boardData[rowPositions][columnPositions] = computer




    return board, continueGames




player = ''
computer = ''
continueGame = True  #True is player #False is computer
boardData =[]

while True:
    print("RESERVEGAM")
    player, computer = choiceGame()
    print()
    print('Player : %s and Computer : %s' %(player,computer))
    boardData = setGame(boardData)
    drawBoard(boardData)
    continueGame = firstPlayer()
    while True:
        key = choosePosition(continueGame,boardData)
        keyPass = str(key)
        columnPosition = int(keyPass[0]) - 1
        rowPosition = int(keyPass[1]) - 1
        boardData,continueGame  = playGame(continueGame,boardData,columnPosition,rowPosition)
        drawBoard(boardData)

