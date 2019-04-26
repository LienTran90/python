#Caesar

import sys

DEFAULT_STRING ='aăâbcdđeêghiklmnoôơpqrstuưvxy'

DEFAULT_LENGTH = len(DEFAULT_STRING)

def inputMessage():
    print('Input your message need to cipher')
    message = input()
    return message

def encryptMessage(encryptMess,encryptPass):
    newMessage = ''
    for index in range(len(encryptMess)):
        if encryptMess[index] != ' ':
            key = DEFAULT_STRING.find(encryptMess[index])
            newKey = key + encryptPass
            if newKey >= DEFAULT_LENGTH:
                newKey = newKey - DEFAULT_LENGTH

            newCharacter = DEFAULT_STRING[newKey]
        else:
            newCharacter = ' '

        newMessage += newCharacter

    return newMessage

def decryptMessage(decryptMess,decryptPass):
    newMessage = ''
    for index in range(len(decryptMess)):
        if decryptMess[index] != ' ':
            key = DEFAULT_STRING.find(decryptMess[index])
            newKey = key - decryptPass
            if newKey < 0:
                newKey =  DEFAULT_LENGTH + newKey

            newCharacter = DEFAULT_STRING[newKey]
        else:
            newCharacter = ' '

        newMessage += newCharacter

    return newMessage

def setKey():
    while True:
        print('')
        mode = input('Enter mode encrypt (number) 1 - %s : ' %(DEFAULT_LENGTH -1))
        try:
            val = int(mode)
            if val > 0 and val <= DEFAULT_LENGTH -1:
                return val
        except ValueError:
            print("That's not an int! It's a string")

def playAgain():
    while True:
        print('Do you want to enter message again?')
        playAgain = input().lower()
        if playAgain.startswith('y'):
            return True
        elif playAgain.startswith('n'):
            sys.exit()

def setMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

while True:
    mode = setMode()
    keyMode = setKey()
    message = inputMessage()
    if mode in ['encrypt', 'e']:
        print(encryptMessage(message,keyMode))
    else:
        print(decryptMessage(message,keyMode))

    playAgain()

