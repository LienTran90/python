import random
import sys
import math

def drawBoard(boardGame):
    headerFooter = ''
    for index in range(1,6):
        headerFooter += ' ' * 9 + str(index)

    print('\t ' + headerFooter)

    header = '0123456789' * 6
    print('\t' + header)
    print()

    for center in range(15):
        centerData = ''
        for elenment in range(60):
            centerData += boardGame[center*60 + elenment]
        print(str(center) + '\t' + centerData + '\t' + str(center))

    print()
    print('\t' + header)
    print('\t ' + headerFooter)

def setBoardData():
    board = []
    for center in range(15):
        for elenment in range(60):
            data = random.randint(0,1)
            if data == 0:
                board.append('~')
            else:
                board.append('`')
    return board

def randomTreasure():
    treasureChest = []
    for index in range(3):
        values = [random.randint(0,59),random.randint(0,14)]
        treasureChest.append(values)

    return treasureChest

def isOnBoard(x, y):
    # Return True if the coordinates are on the board; otherwise, return False.
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(previousMoves):

    print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('You already moved there.')
                continue
            return [int(move[0]), int(move[1])]

        print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')

def checkMove(x,y,chest,board):

    defaultDistance = 100

    for cx,cy in chest:
        currentDistance = math.sqrt(math.pow(cx-x,2) + math.pow(cy-y,2))
        if currentDistance < defaultDistance:
            defaultDistance = currentDistance

        defaultDistance = round(defaultDistance)
        position =  60 * y + x
        if defaultDistance == 0:
            del chest[x][y]
            return board, 'The treasure found !!!'
        else:
            if defaultDistance < 10:
                board[position] = str(defaultDistance)
                return board,'Distance from here to Treasure is %s' %(defaultDistance)
            else:
                board[position] = 'X'
                return board,'Out of range to Treasure'



previousMoves = []
boardGame = setBoardData()
drawBoard(boardGame)
chest = randomTreasure()

while True:
    x,y = makeMove(previousMoves)
    previousMoves.append([x,y])
    boardGame, notification = checkMove(x,y,chest,boardGame)
    drawBoard(boardGame)
    print(notification)


