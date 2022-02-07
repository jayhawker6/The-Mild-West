import os
from easygui import *
import json


# Define Classes

class FatalSystemError(Exception):
    def __init__(self, message="Give the class a string to work with you dummy or it defaults to this!"):
        self.message = message
        super().__init__(self.message)


# Define Functions
def ohgod():  # Let's... Move on.
    msgbox("Let's just move on.", title, "Yeah...")


# Load Data
f = open('json.json')
data = json.load(f)

# Initialize some vars
title = "The Mild West"
buttons = ["Milk", "Slaughter", "Castrate"]
pressed = buttonbox(data['1'], title, buttons)
if pressed == "Milk":
    msgbox(json["3"], title, "What?")  # But something is VERY wrong
    pressed = buttonbox("This is a bull.", title, ["I know what I'm doing!", "What do you mean?", "(Ignore Narrator)"])

    if pressed == "I know what I'm doing!":  # I Know what i'm doing!
        msgbox("Okay, Weirdo. Just saying... That's DISGUSTING.", title, "Shut up and tell the story.")  # Weirdo.
        msgbox("You drink that milk out of that udder and wait... It's real milk? What?", title, "Always Has Been.")

    elif pressed == "What do you mean?":  # What do you mean?
        msgbox(json["2"], title, "So what am I milking?")  # What am I milking?
        pressed = buttonbox("I think you know EXACTLY what you are \"Milking,\" Pardner.", title,
                            ["Oh god...", "No really i'm clueless what is it?"])

        if not pressed == "Oh god...":  # You know what's being milked
            msgbox("The only thing to \"Milk\" down there on a MALE COW is... It's weiner.", title, "Oh god...")
        ohgod()

