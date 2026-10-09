#!bin/python

import time

characters = []
inventory = []
savefile = {

}

def newCharacter(NAME):
    if NAME in characters:
        throwError("Character name is already taken", True)
    characters.append(NAME)
    
def throwError(errorDescription, fatal):
    if fatal == True:
        print("[FATAL] " + errorDescription)
        quit()
    else:
        print("[ERROR] " + errorDescription)

def talk(character, dialogue, delay):
    if character not in characters:
        throwError("Character not found: " + str(character), True)

    splitDialogue = [char for char in dialogue]

    print(f"{str(character)}: ", end='')

    index = 0

    for i in splitDialogue:
        time.sleep(float(delay))
        print(splitDialogue[index], end="", flush=True)
        print("", end="")
        index += 1

    input()

def addToInventory(item):
    inventory.append(item)

def saveState(statName, statValue):
    savefile[statName] = statValue
    print(str(savefile))

def readState(statName):
    statValue = savefile[statName]
    return statValue