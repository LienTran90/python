import random
import sys

GUESS_COUNT = 10
DEFAULT_DIGIT = 10
SECRET_NUMBER = 3

def generateNumber():
    secretNumber = ''
    number = list(range(10))
    random.shuffle(number)

    for index in range(3):
        secretNumber += str(number[index])

    return secretNumber

def checkInput():

    while True:
        inputNumber = input()
        numberList = list(inputNumber)
        if len(numberList) > 2 and len(numberList) <= 3:
            for index in range(3):
                if numberList[index] not in '0123456789':
                    return 0
            return inputNumber
        else:
            print('Input 3 digit, plz')

def tellClues(inputNumber,guessNumber):
    resultList = []
    inputList = list(inputNumber)
    numberList = list(guessNumber)
    for index in range(3):
        if inputList[index] == numberList[index]:
            resultList.append('Fermi')
        elif inputList[index] in numberList:
            resultList.append('Pico')
        else:
            resultList.append('__')

    if len(resultList) == 0:
        return resultList.append('Bagels')
    else:
        if checkGame:
            resultList.sort()
            return ' '.join(resultList)
        else:

            return ' '.join(resultList)

def playAgain():
    playAgain = input().lower()
    if playAgain.startswith('y'):
        return True, 0
    elif playAgain.startswith('n'):
        sys.exit()

difficulty = ''
checkGame = True
guessNumber = ''
guessTime = 0
continued = True

print('Bagels Game')

while difficulty == '':
    print('M - Medium (Right position Digit), H - Hard (Suffer position Digit)')
    difficulty = input().upper()

    if difficulty == 'M':
        checkGame = False
        break

print('I am thinking of a %s-digit number. Try to guess what it is.' %(SECRET_NUMBER))
print('The clues I give are...')
print('When I say: That means:')
print('Bagels None of the digits is correct.')
print('Pico One digit is correct but in the wrong position.')
print('Fermi One digit is correct and in the right position.')

while True:

    if continued:
        secretNumber = generateNumber()

    continued = False
    print('Gues #' + str(guessTime))
    inputNumber = checkInput()
    result = tellClues(inputNumber, secretNumber)
    resultFinish = result.split(' ')
    if len(list(set(resultFinish))) == 1 and list(set(resultFinish))[0] == 'Fermi':
        print('Victory')
        print('Sercert Number : %s' %(secretNumber))
        print('Do you want to play again! (Yes or No)')
        continued, guessTime = playAgain()

    else:
        print(result)
        guessTime += 1

    if guessTime > 10:
        print('Sercert Number : %s' % (secretNumber))
        print('You lose!!! Do you want to play again! (Yes or No)')
        continued, guessTime = playAgain()