#!bin/python

import time

characters = []
inventory = []

def newCharacter(NAME):
    if NAME in characters:
        throwError("Character name is already taken", True)
    characters.append(NAME)
    
def throwError(string : errorDescription, bool : fatal):
    if fatal == True:
        print("[FATAL] " + errorDescription)
        exit
    else:
        print("[ERROR] " + errorDescription)

def talk(character, string : dialogue, delay):
    if character not in characters:
        throwError("Character not found: " + str(character), True)

    splitDialogue = [char for char in dialogue]

    print(f"{str(character)}: ", end='')

    index = 0

    for i in splitDialogue:
        print(splitDialogue[index], end='')
        index += 1
        time.sleep(delay)
    
    index = 0

def addToInventory(item):
    inventory.append(item)