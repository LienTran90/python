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

def computerAutoPlay(computerChoice, currentBoard):
    while True:
        print()
        print('Computer can press 1 - 9 to play')
        enterKey = input()
        if enterKey in '123456789':
            if currentBoard[int(enterKey) - 1] == ' ':
                currentBoard[int(enterKey) - 1] = computerChoice
                break
            else:
                print('This position already has value')
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

def checkWin():
    if (currentBoard[0] == currentBoard[1]) and (currentBoard[1] == currentBoard[2]) and currentBoard[0] != ' ':
        return True, currentBoard[0]
    elif (currentBoard[3] == currentBoard[4]) and (currentBoard[4] == currentBoard[5]) and currentBoard[3] != ' ':
        return True, currentBoard[3]
    elif (currentBoard[6] == currentBoard[7]) and (currentBoard[7] == currentBoard[8]) and currentBoard[6] != ' ':
        return True, currentBoard[6]
    elif (currentBoard[0] == currentBoard[3]) and (currentBoard[3] == currentBoard[6]) and currentBoard[0] != ' ':
        return True, currentBoard[0]
    elif (currentBoard[1] == currentBoard[4]) and (currentBoard[4] == currentBoard[7]) and currentBoard[1] != ' ':
        return True, currentBoard[1]
    elif (currentBoard[2] == currentBoard[5]) and (currentBoard[5] == currentBoard[8]) and currentBoard[2] != ' ':
        return True, currentBoard[2]
    elif (currentBoard[0] == currentBoard[4]) and (currentBoard[8] == currentBoard[8]) and currentBoard[0] != ' ':
        return True, currentBoard[0]
    elif (currentBoard[2] == currentBoard[4]) and (currentBoard[6] == currentBoard[8]) and currentBoard[2] != ' ':
        return True, currentBoard[2]
    else:
        return False, ''

yourChoice = ''
computerChoice = ''
currentBoard = []

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
    else:
        computerAutoPlay(computerChoice, currentBoard)
        firstPlayer = 0

    win, winner = checkWin()
    if win:
        if yourChoice == winner:
            print('You are Victory!!!')
            print()
            showBoard(currentBoard)
        else:
            print('Computer is Victory!!!')
            print()
            showBoard(currentBoard)

        while True:
            print('Do you want to play again? (Yes or No)')
            playAgain = input().lower()
            if playAgain.startswith('y'):
                yourChoice = ''
                computerChoice = ''
                clearBoard()
                break
            elif playAgain.startswith('n'):
                sys.exit()



