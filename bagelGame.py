import random

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
        print('Guess secret Number :')
        inputNumber = input()
        numberList = list(inputNumber)
        for index in range(3):
            if numberList[index] not in '0123456789':
                return 0

        return inputNumber

def tellClues(inputNumber,guessNumber):
    resultList = []
    inputList = list(inputNumber)
    numberList = list(guessNumber)
    for index in range(3):
        if inputList[index] == numberList[index]:
            resultList.append('Pico')
        elif inputList[index] in numberList:
            resultList.append('Fermi')

    if len(resultList) == 0:
        return resultList.append('Bagels')
    else:
        if checkGame:
            return ' '.join(resultList)
        else:
            return ' '.join(resultList)

difficulty = ''
checkGame = True
guessNumber = ''

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

secretNumber = generateNumber()
print(secretNumber + ' ẩn số')
inputNumber = checkInput()
print(inputNumber)
result =  tellClues(inputNumber, secretNumber)

print (result)

