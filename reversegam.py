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
        boardDatas.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    boardDatas[3][3] = 'X'
    boardDatas[3][4] = 'O'
    boardDatas[4][4] = 'X'
    boardDatas[4][3] = 'O'

    return boardDatas


def firstPlayer():
    number = random.randint(0, 1)
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
            print('X', 'O')
            return 'X', 'O'
        elif players.lower() == 'o':
            print('O', 'X')
            return 'O', 'X'


def computerCanMove(chests, boards):
    computerMoves = []
    rangeNumber = ['1', '2', '3', '4', '5', '6', '7', '8']
    duplicateBoard = copyBoard(boards)
    for row in rangeNumber:
        for column in rangeNumber:
            keys = str(column)+str(row)
            if duplicateBoard[int(row) - 1][int(column) - 1] == ' ':
                if len(checkMove(keys, chests, duplicateBoard)) > 0:
                    computerMoves.append((int(column), int(row)))

    return computerMoves

def isCorner(computerMoves):
    isConrners = [(1, 1), (8, 1), (8, 8), (1, 8)]
    for corner in computerMoves:
        if corner in isConrners:
            return corner[0], corner[1]
    return '0', '0'

def computerChoose(boards,computers,player,computerMoves):
    bestScore = 0
    bestRow = ''
    bestColumn = ''
    bestColumn, bestRow = isCorner(computerMoves)

    if bestColumn != '0' and bestRow != '0':
        return bestRow, bestColumn

    for column, row in computerMoves:
        duplicateBoard = copyBoard(boards)
        duplicateBoard[int(row) - 1][int(column) - 1] = computers
        keyss = str(column) + str(row)
        lstMoves = checkMove(keyss, computer, duplicateBoard)
        duplicateBoard = flipChest(lstMoves, computers, keyss, duplicateBoard)
        playerPoints, computerPoints = checkPoint(player, computers, duplicateBoard)

        if bestScore < computerPoints:
            bestScore = computerPoints
            bestRow = str(row)
            bestColumn = str(column)

    return bestRow, bestColumn

def copyBoard(boards):
    duplicateBoard = []
    duplicateBoard = setGame(duplicateBoard)
    for row in range(8):
        for column in range(8):
            duplicateBoard[row][column] = boards[row][column]
    return duplicateBoard


def choosePosition(continueGames, board):
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        if continueGames:
            playerMove = computerCanMove(player, board)
            if len(playerMove) == 0:
                return '0'
            enterkey = input('Enter position to play (11 - 88) : ')
        else:
            computerMove = computerCanMove(computer, board)
            if len(computerMove) == 0:
                return '0'
            print('Computer turn: ')
            row, column = computerChoose(board, computer, player, computerMove)
            enterkey = column + row
            print(enterkey)
            return enterkey
        try:
            if enterkey[0] in DIGITS1TO8 and enterkey[1] in DIGITS1TO8:
                keys = int(enterkey)
                if keys > 10 & keys < 89:
                    if board[int(enterkey[1]) - 1][int(enterkey[0]) - 1] == ' ':
                        return keys
                    else:
                        print('This position have value')
            else:
                print('This move is not valid')
        except ValueError:
            print('Enter number not string')


def playGame(continueGames, board, columnPositions, rowPositions):

    if continueGames:
        continueGames = False

        boardData[rowPositions][columnPositions] = player
    else:
        continueGames = True
        boardData[rowPositions][columnPositions] = computer

    return board, continueGames

def checkPoint(players,computers,board):
    playerPoint = 0
    computerPoint = 0
    for row in range(8):
        for column in range(8):
            if board[row][column] == players:
                playerPoint += 1
            elif board[row][column] == computers:
                computerPoint += 1

    return playerPoint, computerPoint



def checkMove(keys, chests, boards):
    lstCanMove = []
    keyPass = str(keys)
    columnPosition = int(keyPass[0]) - 1
    rowPosition = int(keyPass[1]) - 1
    lstMove = [(0, -1), (0, 1), (1, 0), (-1, 0), (1, -1), (-1, -1), (1, 1), (-1, 1)]
    for positionX, positionY in lstMove:
        checkRow = rowPosition + positionX
        checkColumn = columnPosition + positionY
        if checkRow < 0 or checkRow > 7 or checkColumn < 0 or checkColumn > 7:
            continue

        checkData = boards[checkRow][checkColumn]

        if checkData == ' ' or checkData == chests:
            continue

        while True:
            checkRow += positionX
            checkColumn += positionY
            if checkColumn < 8 and checkRow < 8:
                checkData = boards[checkRow][checkColumn]
                if checkData == chests:
                    lstCanMove.append((positionX, positionY))
                    break
                elif checkData == ' ':
                    break
            else:
                break

    return lstCanMove


def flipChest(lstMove, chests, keys, boards):
    keyPass = str(keys)

    for element in lstMove:
        checkRow = int(keyPass[1]) - 1
        checkColumn = int(keyPass[0]) - 1
        while True:
            checkRow += element[0]
            checkColumn += element[1]
            checkData = boards[checkRow][checkColumn]

            if checkData != chests:
                boards[checkRow][checkColumn] = chests
            elif checkData == chests:
                break
    return boards


def playAgain():
    while True:
        playAgain = input().lower()
        if playAgain.startswith('y'):
            return True, 0
        elif playAgain.startswith('n'):
            sys.exit()

player = ''
computer = ''
continueGame = True  # True is player False is computer
boardData = []

while True:
    print("RESERVEGAM")

    player, computer = choiceGame()
    print()
    print('Player : %s and Computer : %s' %(player, computer))
    boardData = setGame(boardData)
    drawBoard(boardData)

    continueGame = firstPlayer()

    while True:

        key = choosePosition(continueGame, boardData)
        if key == '0':
            break

        lstMoves = []
        chest = ''
        if continueGame:
            lstMoves = checkMove(key, player, boardData)
            chest = player
        else:
            lstMoves = checkMove(key, computer, boardData)
            chest = computer

        if len(lstMoves) > 0:
            keyPass = str(key)
            columnPosition = int(keyPass[0]) - 1
            rowPosition = int(keyPass[1]) - 1
            boardData, continueGame = playGame(continueGame, boardData, columnPosition, rowPosition)

            boardData = flipChest(lstMoves, chest, keyPass, boardData)
            drawBoard(boardData)
            print()
            playerPoint, computerPoint = checkPoint(player, computer, boardData)
            print('Player : %s Point, Computer : %s Point' %(playerPoint, computerPoint))
        else:
            print('This move not valid')

    print('This board is full')
    print()
    playerPoint, computerPoint = checkPoint(player, computer, boardData)
    print('Player : %s Point, Computer : %s Point' % (playerPoint, computerPoint))

    if playerPoint > computerPoint:
        print('Player win!!!')
    else:
        print('Computer win!!!')

    print('Do you want to play again! (Yes or No)')
    playAgain()

