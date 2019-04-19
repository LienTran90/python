import random
import sys

def choiceFirstPlayer():
    randomChoice = random.randint(0, 1)
    if randomChoice == 0:
        print('You begins first')
    else:
        print('Computer begins first')
    print()
    return randomChoice

def showBoard(currentBoard):
    row1 = ' ' + currentBoard[0] + ' | ' + currentBoard[1] + ' | ' + currentBoard[2]

    print(row1)
    print('---+---+---')

    row2 = ' ' + currentBoard[3] + ' | ' + currentBoard[4] + ' | ' + currentBoard[5]
    print(row2)
    print('---+---+---')

    row3 = ' ' + currentBoard[6] + ' | ' + currentBoard[7] + ' | ' + currentBoard[8]
    print(row3)

def getBoardCopy(board):
    # Make a copy of the board list and return it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def computerAutoPlay(currentBoard):
    print()
    print('Computer choices')

    # Check win

    for index in range(1, 10):
        boardCopy = getBoardCopy(currentBoard)
        if boardCopy[int(index) - 1] == ' ':
            boardCopy[int(index) - 1] = computerChoice
            win, winner = checkWin(boardCopy)
            if win:
                currentBoard[int(index) - 1] = computerChoice
                return True

    # Check lose
    for index in range(1, 10):
        boardCopy = getBoardCopy(currentBoard)
        if boardCopy[int(index) - 1] == ' ':
            boardCopy[int(index) - 1] = yourChoice
            win, winner = checkWin(boardCopy)
            if win:
                currentBoard[int(index) - 1] = computerChoice
                return True

    # Check center
    if currentBoard[4] == ' ':
        currentBoard[4] = computerChoice
        return True

    # Check corner

    for element in corner:
        print(element)
        if currentBoard[int(element)] != ' ':
            corner.remove(element)

    if len(corner) > 0:
        currentBoard[int(random.choice(corner))] = computerChoice
        return True

    # Check Column

    for element in column:
        print(element)
        if currentBoard[int(element)] != ' ':
            column.remove(element)

    if len(column) > 0:
        currentBoard[int(random.choice(column))] = computerChoice
        return True

    print()

def youPlay(yourChoice, currentBoard):
    while True:
        print()
        print('You can press 1 - 9 to play')
        enterKey = input()
        if enterKey in '123456789':
            if currentBoard[int(enterKey) - 1] == ' ':
                currentBoard[int(enterKey) - 1] = yourChoice
                break
            else:
                print('This position already has value')
    print()

def checkWin(Board):
    if (Board[0] == Board[1]) and (Board[1] == Board[2]) and Board[0] != ' ':
        return True, Board[0]
    elif (Board[3] == Board[4]) and (Board[4] == Board[5]) and Board[3] != ' ':
        return True, Board[3]
    elif (Board[6] == Board[7]) and (Board[7] == Board[8]) and Board[6] != ' ':
        return True, Board[6]
    elif (Board[0] == Board[3]) and (Board[3] == Board[6]) and Board[0] != ' ':
        return True, Board[0]
    elif (Board[1] == Board[4]) and (Board[4] == Board[7]) and Board[1] != ' ':
        return True, Board[1]
    elif (Board[2] == Board[5]) and (Board[5] == Board[8]) and Board[2] != ' ':
        return True, Board[2]
    elif (Board[0] == Board[4]) and (Board[4] == Board[8]) and Board[0] != ' ':
        return True, Board[0]
    elif (Board[2] == Board[4]) and (Board[4] == Board[6]) and Board[2] != ' ':
        return True, Board[2]
    else:
        return False, ''

yourChoice = ''
computerChoice = ''
currentBoard = []
moves = 0
corner = [0, 2, 6, 8]
column = [1, 3, 5, 7]
def clearBoard():
    for iniData in range(9):
        currentBoard.append(' ')


print('TIC TAC TOE')

while True:
    print('Do you want to choice X or O')
    yourChoice = input().upper()
    if yourChoice == 'X':
        computerChoice = 'O'
        break
    elif yourChoice == 'O':
        computerChoice = 'X'
        break

firstPlayer = choiceFirstPlayer()
clearBoard()

while True:

    showBoard(currentBoard)

    if firstPlayer == 0:
        youPlay(yourChoice, currentBoard)
        firstPlayer = 1
        moves += 1
    else:
        computerAutoPlay(currentBoard)
        firstPlayer = 0
        moves += 1

    win, winner = checkWin(currentBoard)
    if win or moves == 8:
        if yourChoice == winner:
            print('You are Victory!!!')
            firstPlayer = 0
            print()
            showBoard(currentBoard)
        else:
            print('Computer is Victory!!!')
            firstPlayer = 1
            print()
            showBoard(currentBoard)
            print()

        if moves == 8:
            print('Full option')

        while True:
            print('Do you want to play again? (Yes or No)')
            playAgain = input().lower()
            if playAgain.startswith('y'):
                currentBoard = []
                clearBoard()
                moves = 0
                corner = [0, 2, 6, 8]
                column = [1, 3, 5, 7]
                break
            elif playAgain.startswith('n'):
                sys.exit()





