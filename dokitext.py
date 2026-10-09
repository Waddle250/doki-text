#!bin/python

import time
import ast

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

def addToInventory(item : str):
    inventory.append(item)

def saveValue(statName : str, statValue):
    savefile[statName] = statValue
    print(str(savefile))

def readValue(statName : str):
    statValue = savefile[statName]
    return statValue

def save(slot : int):
    saveFile = open(f"save{slot}", "wt")
    data = str(savefile)
    savefile.write(data)

def load(slot):
    saveFile = open(f"save{slot}", "r")
    data = saveFile.read()
    savefile = ast.literal_eval(data)
    