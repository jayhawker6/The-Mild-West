import json

from easygui import *


# Define Classes

class FatalSystemError(Exception):
    def __init__(self, message="Give the class a string to work with you dummy or it defaults to this!"):
        self.message = message
        super().__init__(self.message)


# Define Functions
def ohgod():  # Let's... Move on.
    msgbox("Let's just move on.", title, "Yeah...")


def addwtff(x=1):
    global wtff
    oldwtff = wtff
    wtff += x
    tempstr = "WTF Factor: " + str(oldwtff) + " --> " + str(wtff)
    msgbox(tempstr, "The Mild West", "...What the...")


# Load Data
f = open('json.json')
data = json.load(f)

# Initialize some vars
title = "The Mild West"
strength = 1
stupidity = 1
wtff = 1

# Begin the Bull
while True:
    buttons = ["Milk", "Slaughter", "Castrate"]
    pressed = buttonbox(data["1"], title, buttons)
    if pressed == "Milk":  # Chose to milk the bull
        msgbox(data["3"], title, "What")  # But something is VERY wrong
        buttons = ["I know what I'm doing!", "What do you mean?", "Ignore Narrator"]
        pressed = buttonbox("This is a bull.", title, buttons)

        if pressed == "I know what I'm doing!" or pressed == "Ignore Narrator":  # I Know what i'm doing!
            msgbox("Okay, Weirdo. Just saying... That's DISGUSTING.", title, "Shut up and tell the story.")  # Weirdo.
            msgbox("You drink that milk out of that udder and wait... It's real milk? What!?", title,
                   "Always Has Been...")
            addwtff(2)
            msgbox("How the hell did you do that? Still Disgusting but I applaud. Anyways, Time to move on.", title,
                   "Trudge Onward!")
            break

        elif pressed == "What do you mean?":  # What do you mean?
            msgbox(data["2"], title, "So what am I milking?")  # What am I milking?
            pressed = buttonbox("I think you know EXACTLY what you are \"Milking,\" Pardner.", title,
                                ["Oh god...", "No really i'm clueless what is it?"])
            msgbox(data["4"], title, "I'm sorry!")
            ohgod()
            msgbox("Anyways, Time to move on.", title, "But i'm still hungry!")
            break

    elif pressed == "Castrate":
        pressed = buttonbox("What in tarnation gave you the urge to choose that option!", title,
                            ["*Shrug*", "Nevermind..."])
        if pressed == "*Shrug*":
            pass
        else:
            msgbox("Yeah don't you touch that poor thing! What did it ever do to you, you monster!", title, "I guess")
            break
