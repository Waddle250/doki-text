import dokitext

dokitext.newCharacter("T")
dokitext.newCharacter("")
dokitext.talk("T", "Hey there!")
dokitext.talk("T", "This is the official DokiText example.")
dokitext.talk("T", "Would you like me to explain how this works, or go straight to an example?")
dokitext.saveValue("skipToExample", dokitext.choose("'T' is waiting patiently.", ["Explain please!", "Let's go straight to the example."]))

if dokitext.readValue("skipToExample") == 1:
    dokitext.talk("T", "Alright! Let's get started with the explanation!")
    dokitext.talk("T", "Using 'dokitext.newCharacter()' will add a new character. This character is able to talk by using 'dokitext.talk().'")
    dokitext.talk("T", "I won't explain the rest of these two, as the code for this example is very easy to read.")
    dokitext.talk("T", "Using 'dokitext.saveValue and dokitext.readValue' is also pretty easy. In fact, in the option back there, it was used to store your input so that you could choose whether to read this example or not.")
    dokitext.talk("T", "This explanation is meant to not go in depth, but it's meant to just lightly cover some functions.")

dokitext.talk("T", "Alright! Now let's get to the example!")
dokitext.talk("T", "So... you want some of my sea salt ice cream?")
dokitext.saveValue("knowsBall", dokitext.choose("Will you take the ice cream?", ["Yes", "No"]))

if dokitext.readValue("knowsBall") == 1:
    dokitext.talk("T", "Here. Have it!")
    dokitext.talk("", "SSIceCream was added to your inventory.", 0.1)
    dokitext.addToInventory("SSIceCream")
    dokitext.talk("T", "You seem so happy eating that.")
    dokitext.talk("T", "Here. Let me save for you.")
    dokitext.save(1)
    dokitext.talk("T", "Check out the save file after this, OK?")
    dokitext.talk("T", "It'll help you out a lot seeing it")
else:
    dokitext.talk("T", "I'll eat it myself then.")
    dokitext.talk("T", "Here. Let me save for you.")
    dokitext.save(1)
    dokitext.talk("T", "Check out the save file after this, OK?")
    dokitext.talk("T", "It'll help you out a lot seeing it")
