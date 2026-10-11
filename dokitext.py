#!bin/python

import time
import json

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

def talk(character, dialogue, delay = 0.05):
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

def choose(prompt : str, options : list) -> int:
    print(f"[CHOICE]:  {prompt}")

    for index, option in enumerate(options, 1):
        print(f"{index}: {option}")

    while True:
        choice = input("Select an option: ").strip()

        if choice.isdigit():
            choiceNum = int(choice)
            if 1 <= choiceNum <= len(options):
                return choiceNum
            else:
                print("Please select a valid number.")


def addToInventory(item : str):
    inventory.append(item)

def saveValue(statName : str, statValue):
    savefile[statName] = statValue

def readValue(statName : str):
    statValue = savefile[statName]
    return statValue

def save(slot : int):
    savefile["inventory"] = inventory
    savefile["characters"] = characters
    with open(f"save{slot}.json", "w") as savedState:
        json.dump(savefile, savedState, indent=4)

def load(slot):
    global savefile, inventory, characters
    with open(f"save{slot}.json", "r") as loadedState:
            savefile = json.load(loadedState)
            inventory = savefile.get("inventory", [])
            characters = savefile.get("characters", [])


